import copy
import itertools
import re
import sys
import textwrap
from collections import ChainMap
from io import StringIO
from pathlib import Path
from typing import Callable, Dict, Iterable, List, NamedTuple, Optional, Tuple, Union

from bs4 import BeautifulSoup, NavigableString, Tag

BOLD = "\033[1m"
NC = "\033[0m"
B = "\033[34m"
G = "\033[32m"
W = "\033[37m"

Node = Union[Tag, NavigableString]


class Prototype(NamedTuple):
    header: str
    definition: str


VERBOSE = 0


def extract_until(
    element,
    is_condition: Callable[[Node], bool],
    contains_condition: Callable[[Node], bool],
    depth=0,
) -> Iterable[Node]:
    """Extract all elements until a condition is reached"""
    if VERBOSE:
        print("  " * depth + str(element)[:80].replace("\n", "^N"))
        breakpoint()
    # Do the simple parts - all future elements not containing the tag
    while True:
        if is_condition(element) or contains_condition(element):
            break
        yield element
        element = next_uncontained_element(element)
        if element is None:
            return

    # If we found the tag through direct iteration just return it
    if is_condition(element):
        return
    # Otherwise, it must be one of our children
    for child in element.children:
        if is_condition(child):
            return
        elif contains_condition(child):
            break
        else:
            # It's a child without the condition
            yield child

    if depth > 100:
        breakpoint()
    yield from extract_until(child, is_condition, contains_condition, depth=depth + 1)


def extract_until_tag(element, tags):
    """Extract all elements until we hit a tag, recursing if necessary"""

    def is_tag(el):
        return isinstance(el, Tag) and el.name in tags

    def contains_tag(el):
        return isinstance(el, Tag) and el.find(tags)

    yield from extract_until(element, is_tag, contains_tag)


def extract_until_string(element, strings):
    """Extract all elements until we hit a string"""

    def is_string(el):
        return isinstance(el, NavigableString) and (
            el.string in strings or any(x in el.string for x in strings)
        )

    def contains_string(el):
        return isinstance(el, Tag) and (
            el.find(string=strings) or any(x in el.get_text() for x in strings)
        )

    yield from extract_until(element, is_string, contains_string)


def extract_section(header):
    """Read forward from a tag to get the whole sectio. Return as a <div>."""
    section = []
    section = Tag(name="div")
    section.append(copy.copy(header))
    for t in extract_until_tag(header.next_sibling, {"hr", "h4"}):
        # print(W + str(t).replace("\n", "^N") + NC)
        section.append(copy.copy(t))

    return section


def remove_empty_paragraphs(parent):
    """Remove p tags whose contents are empty"""
    for part in parent:
        if (
            part.name == "p"
            and all(isinstance(x, NavigableString) for x in part.children)
            and not any(x.string.strip() for x in part.children)
        ):
            part.extract()


def remove_string(element, text):
    """Remove any items whose contents is a known fixed string"""
    for part in element:
        if part.string and part.string.strip() == text.strip():
            part.decompose()


def remove_paragraph_newlines(element):
    """Clean up (remove) newlines in pure paragraphs"""
    for para in element("p"):
        if not list(para.strings):
            continue
        if (
            not para.find("p")
            and para.contents
            and all(isinstance(c, NavigableString) for c in para.children)
        ):
            cleanstr = []
            for substring in para:
                cleanstr.append(" ".join(s.strip() for s in substring.splitlines()))
                substring.extract()
            para.insert(0, NavigableString(" ".join(cleanstr)))


def next_uncontained_element(element: Node) -> Optional[Node]:
    """Advance until the next element that is not contained within the argument"""
    if isinstance(element, NavigableString) or not element.descendants:
        return element.next_element

    for next_element in element.next_elements:
        if next_element not in element.descendants:
            return next_element

    return None


def extract_definition(element, section_number=None):
    """Split up and determine definition data from a <div> section"""
    headers = [
        "PROTOTYPE",
        "DESCRIPTION",
        "ARGUMENTS",
        "RETURN VALUE",
        "SEE ALSO",
        "DEFINITION",
    ]

    definition = {}
    if section_number:
        definition["SECTION_NUMBER"] = section_number
    while element:
        if not list(extract_until_string(element, headers)):
            # We are *at* a section header
            # Wind forwards until we get the navigablestring
            while not isinstance(element, NavigableString):
                element = element.next_element
            section = element.string.strip()
            # Move one element past the end of the string
            element = element.next_element
            subsection = Tag(name="div")
            assert section not in definition
            definition[section] = subsection
        else:
            # We're in a preamble?
            subsection = Tag(name="div")
            assert "PREAMBLE" not in definition
            definition["PREAMBLE"] = subsection

        last_part = None
        for part in extract_until_string(element, headers):
            subsection.append(copy.copy(part))
            last_part = part

        assert not [
            x for x in headers if x in subsection.get_text()
        ], "Section should not contain header"

        element = next_uncontained_element(last_part)

    if "ARGUMENTS" in definition:
        definition["ARGUMENTS"] = parse_arguments(definition["ARGUMENTS"])
    if "PROTOTYPE" in definition:
        definition["PROTOTYPE"] = parse_prototype(definition["PROTOTYPE"])
    parse_title_and_preamble(definition)

    return definition


reInclude = re.compile(r'\s*#include "([^"]+)')


def parse_prototype(element):
    """Parse a prototye subsection"""
    header = None
    definitions = []
    prototype_text = element.get_text()
    # Manual override: 2.4.45 has bad definitions
    if "cbf_get_pixel_normal" in prototype_text:
        tn = prototype_text.find("cbf_get_pixel_normal ")
        prototype_text = prototype_text[: tn + 1] + prototype_text[tn + 1 :].replace(
            "cbf_get_pixel_normal ", "cbf_get_pixel_normal_sf"
        )
    for line in prototype_text.splitlines():
        if match := reInclude.match(line):
            header = match.group(1)
            continue
        if not line.strip():
            continue
        if definitions and not (
            definitions[-1].endswith(";") or definitions[-1].endswith(")")
        ):
            definitions[-1] = definitions[-1] + " " + line.strip()
            # print("CONTINUE: " + definitions[-1])
        else:
            definitions.append(line.strip())

    return [
        x._replace(header=header)
        for x in [parse_function_definition(dn) for dn in definitions]
    ]
    # return [Prototype(header, x) for x in definitions]


def parse_arguments(element):
    """Parse an arguments section into argument descriptions"""
    data = []
    table = element.find("table")
    if table:
        table.extract()
    else:
        assert "no arguments" in element.get_text()
        return
    table_body = table.find("tbody")

    rows = table_body.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values

    # Make extra sure the described all the argument data
    assert not element.get_text().strip()
    # Make sure only two elements max
    assert all(len(x) <= 2 for x in data)
    # Pad out if not 2 items
    data = [x if len(x) == 2 else x + [""] for x in data]

    return {
        name: " ".join(line.strip() for line in desc.splitlines())
        for name, desc in data
    }


def parse_title_and_preamble(defn):
    """
    Parse and validate the title entries. Split the title and any preamble.

    Writes back the NAMES section.
    Prepends any remaining PREAMBLE to the DESCRIPTION.
    """
    num = defn["SECTION_NUMBER"]
    assert defn["PREAMBLE"].find("h4")
    header = defn["PREAMBLE"].find("h4").extract()
    # print("    " + header.get_text())
    header_text = header.get_text()
    assert num in header_text
    # We know some of the section headers are wrong
    header_text = fix_known_bad_header_titles(header_text, defn)

    names = list(header_text.replace(num, "").replace(",", " ").split())
    assert len(names) == len(set(names)), f"Section {num} has duplicate titles?"
    defn["NAMES"] = names
    if "PROTOTYPE" in defn:
        assert len(defn["PROTOTYPE"]) == len(names), "Header-prototype length mismatch"

        # checknames = set(names)
        # Check that every header name has a prototype definition
        # assert all(any(name in [x.name for x in proto]) )
        all_protos = {x.name for x in defn["PROTOTYPE"]}
        if not all_protos == set(names):
            breakpoint()
        assert all_protos == set(
            names
        ), f"Not all title names in {num} had prototype definitions"
        # for proto in defn["PROTOTYPE"]:
        #     for name in list(checknames):
        #         if name == proto.name:
        #             checknames.remove(name)
        #             break
        # assert not checknames,

    if defn["PREAMBLE"].get_text().strip():
        # print(defn["PREAMBLE"].get_text().strip())
        if "DESCRIPTION" in defn:
            # Reinject the preamble into the description
            for child in reversed(defn["PREAMBLE"].contents):
                defn["DESCRIPTION"].insert(0, child.extract())
            assert not defn["PREAMBLE"].get_text().strip()
        else:
            defn["DESCRIPTION"] = defn["PREAMBLE"]
    del defn["PREAMBLE"]


def fix_known_bad_header_titles(header_text, definition):
    # Fix some hardcoded known-bad header entries
    if (
        "PROTOTYPE" in definition
        and "cbf_write_file" in header_text
        and "cbf_write_widefile" not in header_text
        and any("cbf_write_widefile" in x.raw for x in definition["PROTOTYPE"])
    ):
        # 2.3.4 missing title entry
        header_text = header_text.replace(
            "cbf_write_file", "cbf_write_file, cbf_write_widefile"
        )
    header_text = (
        header_text.replace("\n", " ")
        .replace("cbf_ ", "cbf_")
        .replace("\xa0", " ")
        .replace(
            "cbf_reset_datablock, cbf_reset_datablock",
            "cbf_reset_datablock, cbf_reset_saveframe",
        )
        .replace(
            "cbf_set_3d_image, cbf_set_3d_image, cbf_set_3d_image",
            "cbf_set_3d_image, cbf_set_3d_image_fs, cbf_set_3d_image_sf,",
        )
        .replace(
            "set_reference_beam_center_fs, set_reference_beam_center_fs",
            "set_reference_beam_center_fs, set_reference_beam_center_sf",
        )
        .replace(
            "cbf_get_detector_axis_slow, cbf_get_detector_axis_slow,",
            "cbf_get_detector_axis_slow, cbf_get_detector_axis_fast,",
        )
        .replace("cbf_get_reference_poise", "cbf_get_axis_reference_poise")
        .replace(" set_reference_beam_center", "cbf_set_reference_beam_center")
        .replace(" set_reference_beam_center", " cbf_set_reference_beam_center")
    )
    return header_text


def get_section_headers(
    soup: BeautifulSoup, all_sections: Iterable[str]
) -> Dict[str, str]:
    """
    Given a list of section numbers, extract a dictionary of titles

    Args:
        soup: The Beautify Soup object
        all_sections: List of sections e.g. ["2.3.1", "2.4.5"]. This will
            be used to generate a list of "minor" sections ["2.3", "2.4"],
            and the section titles will be extracted for those numbers.
    """
    sectionhead = re.compile(r"^\d+\.\d+")
    for section in set(itertools.chain(*[sectionhead.findall(x) for x in defs])):
        # Get the description of this from the a
        sectiontitle = soup.find("a", attrs={"name": section})
        if sectiontitle:
            sec = sectiontitle.string
        else:
            sectiontitle = soup.find("div", attrs={"id": section})
            sec = sectiontitle.find(["h2", "h4"]).string

        sections[section] = sec.replace(section + " ", "").strip()


def split_with_nested(splitter: str, string: str, keep_splitter: str = "") -> List[str]:
    """
    Split a string on a character, ignoring nested parentheses.

    Args:
        splitter: The characters to split on
        string: The string to split
        keep_splitter: These split characters will be included as arguments on their own
    """
    args = []
    cur_arg = ""
    in_subarg = 0
    for c in string:
        if c == "(":
            in_subarg += 1
        elif c == ")":
            in_subarg -= 1

        if not in_subarg and c in splitter:
            if cur_arg.strip():
                args.append(cur_arg.strip())
            if c in keep_splitter:
                args.append(c)
            cur_arg = ""
        else:
            cur_arg += c
    if cur_arg:
        args.append(cur_arg.strip())
    return args


class FunctionPrototype(NamedTuple):
    name: str
    ret: Tuple[str]
    args: Tuple[str]
    raw: str
    header: str = None


class FunctionArgument(NamedTuple):
    type: str
    const: bool
    name: str


def parse_function_argument(arg):
    if "(" in arg:
        # We're complex - just skip this parsing
        return FunctionArgument(type=[arg], const=None, name="")
    args = split_with_nested(" *", arg, keep_splitter="*")
    # if args[0] == "const"
    const = False
    if args[0] == "const":
        args = args[1:]
        const = True

    return FunctionArgument(type=tuple(args[:-1]), name=args[-1], const=const)


def parse_function_definition(definition):
    split_parts = re.compile(r"^([^(]+)\((.*)\);?$")
    return_and_name, all_args = split_parts.match(definition).groups()
    pre_types = split_with_nested("* ", return_and_name, keep_splitter="*")
    raw_args = split_with_nested(",", all_args)

    args = [parse_function_argument(arg) for arg in raw_args]
    proto = FunctionPrototype(
        name=pre_types[-1], ret=tuple(pre_types[:-1]), args=tuple(args), raw=definition
    )
    return proto
    print("   ", pre_types)
    print("   ", args)


# Parse the soup
sys.setrecursionlimit(8096)
data = (Path.cwd() / "cbflib" / "doc" / "CBFlib.html").read_text(errors="ignore")
soup = BeautifulSoup(data, "html5lib")

# Find all headers in sections 2.3+
rePrototype = re.compile(r"^2\.[346789]\d*\.")
h4s = [x for x in soup.find_all("h4") if rePrototype.match(x.text)]

# Turn the list of headers into a list of sections (the whole block of tags)
sections = {}
for tag in h4s:
    number = tag.text.split()[0]
    sections[number] = extract_section(tag)

# Extract all sections
defs = {n: extract_definition(section, n) for n, section in sections.items()}


# A list of objects we want to bind, and the lifecycle methods for them
objects_lifecycle_methods = {
    "cbf_handle": ("cbf_make_handle", "cbf_free_handle"),
    "cbf_detector": [],
    "cbf_goniometer": [],
    "cbf_positioner": [],
    "cbf_h5handle": [],
    "cbf_config": ("cbf_config_create", "cbf_config_free"),
}

re_multiple_newlines = re.compile(r"\n\n\n+")


def format_description(desc):
    # if "cbf_get_axis_poise" in desc.get_text():
    #     breakpoint()
    out = (
        re_multiple_newlines.sub("\n\n", desc.get_text().strip())
        .replace("\xa0", " ")
        .replace("*", "\\*")
    )
    # Dedent everything except the first line....
    ddlines = out.splitlines()
    out = ddlines[0] + "\n" + textwrap.dedent("\n".join(ddlines[1:]))
    return out


DOC_ROOT = Path(__file__).parent / "docs"

for root_object in objects_lifecycle_methods:
    output = StringIO()
    # Find all methods which take this object as the first argument
    obj_methods = [
        defn
        for n, defn in defs.items()
        if "PROTOTYPE" in defn
        and defn["PROTOTYPE"]
        and defn["PROTOTYPE"][0].args
        and defn["PROTOTYPE"][0].args[0].type[0] == root_object
    ]

    # Make a "Reverse" lookup for each object method
    members = dict(
        ChainMap(
            *[{proto: defn for proto in defn["PROTOTYPE"]} for defn in obj_methods]
        )
    )
    # For now, use the order from the CBFlib.html
    members_order = sorted(
        members.keys(), key=lambda x: (members[x]["SECTION_NUMBER"], x.name)
    )
    assert all(x.name.startswith("cbf_") for x in members)
    assert len(set(x.name for x in members)) == len(members)
    root_classname = f"{root_object}_struct"

    domain_defs = [f"{root_classname}\n{'*'*len(root_classname)}"]
    domain_defs.append(f".. py:class:: {root_classname}")

    print([x.name for x in members_order[:10]])
    for member, defn in zip(members_order, [members[x] for x in members_order]):
        # Don't document the constructor or destructor
        if member.name in objects_lifecycle_methods[root_object]:
            continue
        # Now emit the definition for each
        entries = [
            f".. py:method:: {root_classname}.{member.name.replace('cbf_', '')}({', '.join(x.name for x in member.args[1:])})"
        ]
        entries.append("")
        entries.append(textwrap.indent(format_description(defn["DESCRIPTION"]), "   "))
        entries.append("")
        # Do parameters
        for param in member.args[1:]:
            # Find this arg in the definition
            # assert param.name in defn["ARGUMENTS"]

            if param.name in defn["ARGUMENTS"]:
                arg_desc = defn["ARGUMENTS"][param.name]
            else:
                arg_desc = ""
            entries.append(f"   :param {param.name}: {arg_desc}".rstrip())
        domain_defs.append("\n".join(entries))

    (DOC_ROOT / "objects" / f"{root_object}.rst").write_text("\n\n".join(domain_defs))


# breakpoint()
# # breakpoint()
# parse_function_definition(
#     "int cbf_H5Drequire_scalar_F64LE2_ULP (const hid_t location, hid_t *const dataset, const char *const name, const double value, int(*cmp)(const void *, const void *, size_t, const void *), const void *const cmp_params)"
# )
# parse_function_definition("cbf_config_t* cbf_config_create ()")
