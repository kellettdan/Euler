# Project Euler: Problem 9
# Special Pythagorean triplet
# Uses: Loops, modulo, if, print
# Import: math package

# Problem set-up
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Import the math package
import math

# Set up a function called p9 where x is the sum of the triplet
def p9(x):

# Loop for i, j, and k from 1 to x (this is very brute force and there must be a more elegant approach)
    for i in range(1,x):
        for j in range(1,x):
            for k in range(1,x):
# Test if the triplet is pythagorean
                if i**2 + j**2 == k**2:
# Test if the triplet sums to x
                    if i + j + k == x:
# Print the product
                        print(i*j*k)
        
p9(1000)