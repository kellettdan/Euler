# Project Euler: Problem 5
# Smallest multiple
# Uses: Loops, modulo, if, print, factorials
# Import: math package

# Problem set-up
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Import the math package
import math

# Set up a function called p5
def p5(x):

# Intialise max_val to x! which we know is a solution (if not the minumum possible)
# Intialise min_j to be the current lowest solution
    max_val = math.factorial(x) + 1
    min_j = max_val

# Loop from 9699690 (product of all primes from 1 to 20) to maximum value
    for j in range(9699690,max_val):
# Check for each value of j if it is divisible by each number in the range
        k=0
        for i in range(1,x+1):
            if (j % i == 0):
                k=k+1
# If k equals the number of distinct numbers then k is a valid solution. If so then break & print
        if k==x:
            min_j=j
            break
    print(min_j)

if __name__ == "__p5__":
    p5(20)