import copy
import itertools
import re
import sys
from pathlib import Path
from typing import Callable, Iterable, NamedTuple, Optional, Union

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

    return [Prototype(header, x) for x in definitions]


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

        checknames = set(names)
        # Check that every header name has a prototype definition
        for proto in defn["PROTOTYPE"]:
            for name in list(checknames):
                if name in proto.definition:
                    checknames.remove(name)
                    break
        assert not checknames, f"Not all title names in {num} had prototype definitions"

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
        and any("cbf_write_widefile" in x.definition for x in definition["PROTOTYPE"])
    ):
        # 2.3.4 missing title entry
        header_text = header_text.replace(
            "cbf_write_file", "cbf_write_file, cbf_write_widefile"
        )
    header_text = (
        header_text.replace("cbf_ ", "cbf_")
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
    )
    return header_text


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
    print(number)
    sections[number] = extract_section(tag)
    print(".....length =", len(str(sections[number])))

# sections = {tag.text.split()[0]: extract_section(tag) for tag in h4s}


# breakpoint()
# pprint(extract_definition(sections["2.3.55"]))
# sys.exit(1)
# breakpoint()
# Extract all sections
defs = {n: extract_definition(section, n) for n, section in sections.items()}
# defs = {}
# for n, section in sections.items():
#     try:
#         defs[n] = extract_definition(section)
#     except:
#         print("Failed on:", n)
#         raise

# Print all the sections nicely, with colour
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


# print("no arguments")
# for num, defn in defs.items():
#     if "ARGUMENTS" in defn:
#         pass
#         # print(num)
#         # print(defn["ARGUMENTS"])
#     else:
#         print(num)

sectionhead = re.compile(r"^\d+\.\d+")

sections = {}
for section in set(itertools.chain(*[sectionhead.findall(x) for x in defs])):
    # Get the description of this from the a
    sec = soup.find("a", attrs={"name": section})
    sections[section] = sec
# section_links = [x for x in soup.find_all("a") if ]
breakpoint()
# # # Now let's try parsing the arguments list
# # print(cm["ARGUMENTS"])
# # print(parse_arguments(cm["ARGUMENTS"]))
# # print(cm["ARGUMENTS"])
# # breakpoint()
