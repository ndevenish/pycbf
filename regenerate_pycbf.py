#!/usr/bin/env python3
from __future__ import absolute_import, division, print_function

import logging
import os.path
import re
import subprocess
import sys

try:
    from typing import List, Optional, Tuple
except ImportError:
    pass


ROOT_DIR = os.path.dirname(__file__)
CBFLIB_DIR = os.path.join(ROOT_DIR, "cbflib")

PY2 = sys.version_info < (3, 0)

if PY2:
    FileNotFoundError = OSError


def check_call(command, *args, **kwargs):
    command_str = command if isinstance(command, str) else " ".join(command)
    print("\n\nRunning", command_str)
    print("=" * (len(command_str) + len("Running ")))

    return subprocess.check_call(command, *args, **kwargs)


def check_output(command, *args, **kwargs):
    print("Running ", command if isinstance(command, str) else " ".join(command))
    return subprocess.check_output(command, *args, **kwargs)


def check_tool(
    name, version_args=[], version_re=None, expect_fail=False, minimum_version=None
):
    # type: (str, List[str], Optional[str], bool, Tuple[int]) -> bool
    """
    Checks if an external tool is present

    Args:
        name: The name of the command
        version_args: Any extra arguments to request version number printing
        version_re: The regex string to extract the version number
        expect_fail: Will the command fail to run if
    """
    print(("Checking " + name + ": ").ljust(20), end="")
    try:
        output = subprocess.check_output(
            [name] + version_args, stderr=subprocess.STDOUT
        )
        output = output.decode("utf-8")
    except FileNotFoundError:
        print("FAIL")
        return False
    except subprocess.CalledProcessError:
        if not expect_fail:
            print("FAIL")
            return False
    if version_re:
        version = re.search(version_re, output)
        if not version:
            print("FAIL")
            logger.warning("Warning: Could not extract version for %s", name)
            return False
        version_str = version.group(1)
        ver = tuple(int(x) for x in re.split(r"[-.]", version_str))
        if ver < minimum_version:
            print("FAIL")
            logger.error(
                "%s version too low:  %s < %s",
                name,
                ".".join(ver),
                ".".join(minimum_version),
            )
            return False
        print("OK  " + ".".join(str(x) for x in ver))
    else:
        print("OK  ")
    return True


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(format="%(message)s")

    # Verify that we have the right versions of everything to regenerate
    tools_available = {
        "nuweb": check_tool("nuweb", expect_fail=True),
        "latex": check_tool("latex", ["-v"]),
        "dvipdfm": check_tool("dvipdfm", ["--version"]),
        "git": check_tool("git", ["--version"]),
        "swig": check_tool(
            "swig", ["-version"], r"SWIG Version (\d[^\s]+)", minimum_version=(4, 0, 0)
        ),
    }

    try:
        browser_dump_tool = next(
            n for n in ["links", "lynx", "elinks"] if check_tool(n, ["-version"])
        )
    except StopIteration:
        sys.exit("Error: Could not find browser dumping tool [lynx, links]")

    could_not_find = {x for x in tools_available if not tools_available[x]}
    if could_not_find:
        sys.exit("Error: Some regeneration tooling is missing. Cannot regenerate.")

    # Reset the sub-repository
    try:
        check_call(
            ["git", "diff", "--no-ext-diff", "--quiet"],
            cwd=os.path.join(ROOT_DIR, "cbflib"),
        )
    except subprocess.SubprocessError:
        # We have changes - reset it
        print("cbflib subdirectory has changes - resetting to reapply")
        check_call(["git", "reset", "--hard", "HEAD"], cwd=CBFLIB_DIR)
    else:
        print("\nNo changes - OK to continue\n")

    print("Starting regeneration")
    regen_dir = os.path.join(CBFLIB_DIR, "pycbf")
    html_file = os.path.join(CBFLIB_DIR, "doc", "CBFlib.html")

    check_call(["nuweb", "pycbf"], cwd=regen_dir)
    check_call(["latex", "pycbf"], cwd=regen_dir)
    check_call(["nuweb", "pycbf"], cwd=regen_dir)
    check_call(["latex", "pycbf"], cwd=regen_dir)
    check_call(["dvipdfm", "pycbf"], cwd=regen_dir)
    check_call(["nuweb", "pycbf"], cwd=regen_dir)
    dumped_html = check_output([browser_dump_tool, "-dump", str(html_file)])
    with open(os.path.join(regen_dir, "CBFlib.txt"), "wb") as f:
        f.write(dumped_html)

    if not PY2:
        # Run 2to3 on make_pycbf.py so we can run it
        make_pycbf = os.path.abspath(os.path.join(regen_dir, "make_pycbf.py"))
        check_call(["2to3", "-w", make_pycbf], cwd=regen_dir)
        check_call([sys.executable, make_pycbf], cwd=regen_dir)

    # Finally, regenerate with swig
    check_call(["swig", "-v", "-python", "pycbf.i"], cwd=regen_dir)

    # Take the pycbf.py, move it to this folder and add the header line
    print("\n\nCopying over and amending pycbf.py")
    with open(os.path.join(regen_dir, "pycbf.py"), "rb") as f:
        pycbf_data = f.read()
    with open(os.path.join(ROOT_DIR, "src", "pycbf", "__init__.py"), "wb") as f:
        f.write(
            b"# AUTOMATICALLY GENERATED BY PYCBF WRAPPER - DO NOT EDIT\n# coding: utf-8\n#\n"
            + pycbf_data
        )
    # Copy over the .c file to build
    print("Copying over and amending pycbf_wrap.c...")
    with open(os.path.join(regen_dir, "pycbf_wrap.c"), "rb") as f:
        pycbf_wrap = f.read()
    # Rewrite the include to cbf.h etc
    pycbf_wrap_rewritten = pycbf_wrap.replace(b"../include/cbf", b"cbf")
    with open(os.path.join(ROOT_DIR, "pycbf_wrap.c"), "wb") as f:
        f.write(pycbf_wrap_rewritten)

    print("done.")
