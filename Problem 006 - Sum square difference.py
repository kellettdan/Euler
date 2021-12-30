# Project Euler: Problem 6
# Sum square difference
# Uses: Loops, if, print
# Import: math package

# Problem set-up
# The sum of the squares of the first ten natural numbers is...
# The square of the sum of the first ten natural numbers is...
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is...
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Import the math package
import math

# Set up a function called p6
def p6(terms):
    ssq=0
    sqs=0
# Calculate sum of squares
    for x in range(1,terms+1):
        ssq=ssq+(x**2)
# Calculate square of sum
    for y in range(1,terms+1):
        sqs=sqs+y
    sqs=sqs**2
# Calculate the difference and print
    diff=sqs-ssq
    print(diff)
        
p6(100)