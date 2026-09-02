#!/usr/bin/env python3
"""
Checks a reflection markdown file (SUBMISSION.md or ARCHITECTURE.md) has
every required heading, and that each section has real content under it —
not just the heading itself, and not a one-line brush-off.

Usage: check_reflection.py <file> <min_words_per_section> <heading1> <heading2> ...
"""
import re
import sys

path = sys.argv[1]
min_words = int(sys.argv[2])
required_headings = sys.argv[3:]

results = []


def check(label, ok):
    results.append((label, ok))
    print(f"{'PASS' if ok else 'FAIL'}: {label}")


try:
    with open(path) as f:
        text = f.read()
except FileNotFoundError:
    print(f"FAIL: {path} does not exist")
    sys.exit(1)

# Strip HTML comments (the instructional placeholders) before counting words,
# so leaving the template comment in place doesn't count as "an answer".
text_no_comments = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

# Split on markdown ## headings
sections = re.split(r"^## +(.+)$", text_no_comments, flags=re.MULTILINE)
# sections = ['', heading1, body1, heading2, body2, ...]
found = {}
for i in range(1, len(sections), 2):
    heading = sections[i].strip()
    body = sections[i + 1].strip() if i + 1 < len(sections) else ""
    found[heading] = body

for heading in required_headings:
    if heading not in found:
        check(f"section '## {heading}' exists", False)
        continue
    word_count = len(found[heading].split())
    check(
        f"'## {heading}' has real content ({word_count}/{min_words} words minimum)",
        word_count >= min_words,
    )

if any(not ok for _, ok in results):
    sys.exit(1)
