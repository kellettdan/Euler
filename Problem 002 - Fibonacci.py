# Project Euler: Problem 2
# Fibonacci
# Uses: Loops, modulo, retaining values, if, print

# Problem set-up
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Set up a function called p2
def p2():

# Initialise variables x, y, z, p & a
# x will keep a running sum of terms to ensure the total does not exceed 4 million
# y will act as the previos Fibonacci number to x
# z will be a temporary term to help keep track of terms
# p will increment by 1 every step in the while loop to number the terms
# a will be the sum of the even valued terms
    x=1
    y=1
    z=0
    p=1
    a=0

# Set up a while loop until the value of the last Fibonacci number exceeds 4 million
    while x < 4000001:
# Set up an if loop to keep just the even values (these will always be p=2 (modulo 3))
        if (p % 3 == 2): 
# For given terms add to a and print
            a=a+x
            print(a)
# Increment p, x, y & z for the next step
        p=p+1
        z=x
        x=x+y
        y=z
        

if __name__ == "__p2__":
    p2()