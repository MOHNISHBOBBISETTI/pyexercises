"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:Any sentence typed by the user.
# 2. Process:Use four built-in Python string tools: .strip(), .upper(), .lower(), and .replace().
# 3. Out: Four different versions of the typed sentence.
# 4. My four transformations, and when each is useful:
#    - strip(): Removes extra spaces at the beginning and end of text.
#    - upper(): Makes all letters capital for clear titles or warnings.
#    - lower(): Makes all letters lowercase to easily compare text.
#    - replace(" ", "_"): Swaps spaces for underscores to create clean file names.

# Your code below
# - strip(): Removed the spaces on the outside as expected.
# - upper(): Made all letters capital as expected.
# - lower(): Made all letters small as expected.
# - replace(" ", "_"): Replaced every space with "_" as expected.
text = input("Type any sentence: ")
print("1. Without extra spaces on ends:", text.strip())
print("2. All uppercase:", text.upper())
print("3. All lowercase:", text.lower())
print("4. With underscores instead of spaces:", text.replace(" ", "_"))