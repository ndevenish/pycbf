import copy
import re
import sys
from pathlib import Path
from pprint import pprint

import bs4


# Read each header until we hit an <hr>
def extract_section(header):
    section = []  # soup.new_tag("div")
    section = bs4.Tag(name="div")
    section.append(copy.copy(header))
    for t in header.next_siblings:
        if t.name == "hr":
            break
        section.append(copy.copy(t))

    return section


def remove_empty_paragraphs(parent):
    """Remove p tags whose contents are empty"""
    for part in parent:
        if (
            part.name == "p"
            and all(isinstance(x, bs4.NavigableString) for x in part.children)
            and not any(x.string.strip() for x in part.children)
        ):
            part.extract()


def remove_string(element, text):
    """Remove any items whose contents is a known fixed string"""
    for part in element:
        if part.string and part.string.strip() == text.strip():
            part.decompose()
            # print("Removing", str(part.extract()).replace("\n", "^N"))


def remove_paragraph_newlines(element):
    """Clean up newlines in pure paragraphs"""
    for para in element("p"):
        if not list(para.strings):
            continue
        if (
            not para.find("p")
            and para.contents
            and all(isinstance(c, bs4.NavigableString) for c in para.children)
        ):
            cleanstr = []
            for substring in para:
                cleanstr.append(" ".join(s.strip() for s in substring.splitlines()))
                substring.extract()
            para.insert(0, bs4.NavigableString(" ".join(cleanstr)))
            print(" ".join(cleanstr))


def extract_definition(section):
    # Find the sections; PROTOTYPE, DESCRIPTION, ARGUMENTS, "RETURN VALUE"
    headers = ["PROTOTYPE", "DESCRIPTION", "ARGUMENTS", "RETURN VALUE", "SEE ALSO"]
    defn = {}
    current_part = None
    for part in section:
        text = part.text if hasattr(part, "text") else part.string
        if text is None:
            break
        for header in headers:
            if header in text:
                current_part = header
                assert header not in defn
                defn[header] = bs4.Tag(name="div")
                defn[header].append(copy.copy(part))
                break
        else:
            if current_part:
                defn[current_part].append(copy.copy(part))
    # For each section, strip out the header part
    for header, parts in defn.items():
        for part in parts:
            h_tag = part.find(string=header)
            if h_tag:
                assert h_tag.parent.name == "b"
                h_tag.parent.decompose()
                #                 print("Removing:", h_tag.parent.extract())
                break
        remove_empty_paragraphs(parts)
        remove_paragraph_newlines(parts)
    remove_string(defn["PROTOTYPE"], '#include "cbf.h"')
    return defn


# Parse the soup
sys.setrecursionlimit(4305)
data = (Path.cwd() / "cbflib" / "doc" / "CBFlib.html").read_text(errors="ignore")
soup = bs4.BeautifulSoup(data, "html5lib")

# Find all headers in sections 2.3+
rePrototype = re.compile(r"^2\.[3-9]\d*\.")
h4s = [x for x in soup.find_all("h4") if rePrototype.match(x.text)]
# Turn the list of headers into a list of sections
sections = {tag.text.split()[0]: extract_section(tag) for tag in h4s}


ed = extract_definition(sections["2.3.2"])
pprint(ed)

# for part in ed.values():
#     remove_paragraph_newlines(part)


# ps = ed["PROTOTYPE"]("p")
# ps
