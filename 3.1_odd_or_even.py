"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What happens on 0, on a negative number, on a very large number:


# Your code below
# Ask for an integer number
N = int(input("Enter a positive number N: "))

# Check for edge cases first using simple if/elif statements
if N < 0:
    print("Error: Negative numbers are not allowed.")
elif N == 0:
    print("There are no numbers to count between 1 and 0.")
elif N > 1000:
    print("Error: Please enter a number 1000 or less so the list isn't too long.")
else:
    # Loop from 1 up to N
    for i in range(1, N + 1):
        # % 2 finds the remainder after dividing by 2.
        # If remainder is 0, it's even. Otherwise, it's odd.
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")