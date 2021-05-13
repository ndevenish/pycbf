import copy
import re
import sys
from pathlib import Path
from pprint import pprint
from typing import NamedTuple

from bs4 import BeautifulSoup, NavigableString, Tag

BOLD = "\033[1m"
NC = "\033[0m"
B = "\033[34m"
G = "\033[32m"


class Prototype(NamedTuple):
    header: str
    definition: str


def extract_until(element, tags, depth=0):
    """Extract all elements until we hit a tag, recursing if necessary"""

    def is_tag(el):
        return isinstance(element, Tag) and any(element.name == tag for tag in tags)

    def contains_tag(el):
        return isinstance(element, Tag) and any(element.find(tag) for tag in tags)

    # Do the simple parts - all future siblings not containing the tag
    prev_element = None
    while True:
        if is_tag(element) or contains_tag(element):
            break
        yield element
        prev_element = element
        element = element.next_sibling
        # It's possible that we reach the end of the initial chain of
        # siblings before finding the next stop-tag. In this case, we
        # want to "iterate out" of this dead end.
        if element is None:
            assert (
                depth == 0
            ), "Something went wrong if stepping out of dead end while recursing"
            # We already emitted the previous element, so move over next
            # elements until the prev_element doesn't contain the new one
            element = prev_element.next_element
            # If it's not a tag - then it doesn't have children. Safe to step out.
            while isinstance(prev_element, Tag) and element in prev_element.descendants:
                element = element.next_element

    # If we found the tag through direct iteration just return it
    if is_tag(element):
        return
    # Otherwise, it must be one of our children
    for child in element.children:
        # If it's not the tag or doesn't contain - pass over
        while not is_tag(child) and not contains_tag(child):
            yield child
        # Maybe this child *is* the tag?
        if is_tag(child):
            return
        # This child must contain the tag - stop this loop then recurse
        break
    yield from extract_until(child, tags, depth=depth + 1)


def extract_section(header):
    """Read forward from a tag to get the whole sectio. Return as a <div>."""
    section = []
    section = Tag(name="div")
    section.append(copy.copy(header))
    for t in extract_until(header.next_sibling, {"hr", "h4"}):
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


def extract_definition(section):
    """Split up and determine definition data from a <div> section"""
    headers = [
        "PROTOTYPE",
        "DESCRIPTION",
        "ARGUMENTS",
        "RETURN VALUE",
        "SEE ALSO",
        "DEFINITION",
    ]
    defn = {}
    current_part = None

    for part in section:
        text = part.get_text() if isinstance(part, Tag) else part.string
        if text is None:
            break
        for header in list(headers):
            if header in text:
                current_part = header
                headers.remove(header)
                assert header not in defn
                defn[header] = Tag(name="div")
                defn[header].append(copy.copy(part))
                break
        else:
            if current_part:
                defn[current_part].append(copy.copy(part))
            elif (
                isinstance(part, Tag)
                and (part.find("h4") or part.name == "h4")
                and "TITLE" not in defn
            ):
                defn["TITLE"] = part
            else:
                defn.setdefault("PREAMBLE", Tag(name="div")).append(copy.copy(part))

    # For each section, strip out the header part
    for header, parts in defn.items():
        for part in parts:
            if isinstance(part, NavigableString):
                continue
            h_tag = part.find(string=header)
            if h_tag:
                assert h_tag.parent.name == "b" or h_tag.parent.name == "strong"
                h_tag.parent.decompose()
                break
        remove_empty_paragraphs(parts)
        remove_paragraph_newlines(parts)
    # if "PROTOTYPE" in defn:
    #     remove_string(defn["PROTOTYPE"], '#include "cbf.h"')
    return defn


reInclude = re.compile(r'\s*#include "([^"]+)')


def parse_prototype(element):
    """Parse a prototye subsection"""
    header = None
    definitions = []
    for line in element.get_text().splitlines():
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

    return [Prototype(header, x) for x in definitions]


# Parse the soup
sys.setrecursionlimit(4305)
data = (Path.cwd() / "cbflib" / "doc" / "CBFlib.html").read_text(errors="ignore")
soup = BeautifulSoup(data, "html5lib")

# Find all headers in sections 2.3+
rePrototype = re.compile(r"^2\.[346789]\d*\.")
h4s = [x for x in soup.find_all("h4") if rePrototype.match(x.text)]

# Turn the list of headers into a list of sections (the whole block of tags)
sections = {tag.text.split()[0]: extract_section(tag) for tag in h4s}


def parse_arguments(element):
    """Parse an arguments section into argument descriptions"""
    data = []
    table = element.find("table").extract()
    table_body = table.find("tbody")

    rows = table_body.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values
    # Make extra sure the described all the argument data
    if element.get_text().strip():
        breakpoint()
    assert not element.get_text().strip()
    # Make sure only two elements
    assert all(len(x) == 2 for x in data)
    return {
        name: " ".join(line.strip() for line in desc.splitlines())
        for name, desc in data
    }


# # Let's try extracting from sections as text - this html is awful
# for num, section in sections.items():
#     text = section.get_text().splitlines()
#     cnt = {}
#     headers = [
#         "PROTOTYPE",
#         "DESCRIPTION",
#         "ARGUMENTS",
#         "RETURN VALUE",
#         "SEE ALSO",
#         "DEFINITION",
#     ]
#     cnt["TITLE"] = text[0]
#     current_section = "PREAMBLE"
#     for line in text[1:]:
#         if line.strip().upper() in headers:
#             current_section = line.strip()
#             cnt[current_section] = Tag(name="div")
#             continue
#         cnt.setdefault(current_section, Tag(name="div")).append(line + "\n")
#     # Handle prototype
#     cnt["PROTOTYPE"] = parse_prototype(cnt["PROTOTYPE"])
#     # cnt["ARGUMENTS"] = parse_arguments(cnt["ARGUMENTS"])
#     breakpoint()

# breakpoint()
# Extract all sections
defs = {n: extract_definition(section) for n, section in sections.items()}
# for n, section in sections.items():
#     # print(n)
#     try:
#         defs[n] = extract_definition(section)
#     except:
#         print("Failed on:", n)
#         raise

# print(defs["2.4.14"])
breakpoint()
extract_definition(sections["2.3.66"])

# # Print all the sections nicely, with colour
# import itertools
# for c, defn in zip(itertools.cycle([B, G]), defs):
#     print(c, type(c), repr(c))
#     print(f"{c}{defn}:")
#     pprint(defs[defn])
#     print(NC)


# # Extract and Print prototypes
# for n, defn in defs.items():
#     print(n)
#     if "PROTOTYPE" in defn:
#         # if n == "2.3.62":
#         #     breakpoint()
#         proto = parse_prototype(defn["PROTOTYPE"])
#         assert proto
#         if len(proto) > 0:
#             for p in proto:
#                 print("PROTO", n, p)

cm = defs["2.3.3"]
pprint(cm)
print()
pprint(parse_prototype(cm["PROTOTYPE"]))
print()


# for num, defn in defs.items():
#     if "ARGUMENTS" in defn:
#         print(num)
#         print(parse_arguments(defn["ARGUMENTS"]))

# # # Now let's try parsing the arguments list
# # print(cm["ARGUMENTS"])
# # print(parse_arguments(cm["ARGUMENTS"]))
# # print(cm["ARGUMENTS"])
# # breakpoint()
