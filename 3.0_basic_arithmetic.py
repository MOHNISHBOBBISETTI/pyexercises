"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What happens when the second number is zero, and why:


# Your code below
# 1. In: Two numbers entered by the user.
# 2. Process: Convert inputs to float (decimal numbers), check that the second number is not zero, and calculate +, -, *, and /.
# 3. Out: The results of adding, subtracting, multiplying, and dividing the numbers.
# 4. What happens when the second number is zero, and why:
#    Decision: Keep asking the user for a new second number until it is not zero.
#    Reasoning: Dividing by zero is impossible in math and crashes Python with an error.

# CHECK IT YOURSELF OBSERVATIONS:
# 7 divided by 2 gives 3.5 because float() allows decimal results.


# Your code below
# Ask the user for two numbers and convert them to float so decimals work
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# If the second number is 0, ask again until the user gives a valid number
while num2 == 0:
    print("You cannot divide by zero! Please try again.")
    num2 = float(input("Enter a second number that is NOT zero: "))

# Print the four math calculations
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)