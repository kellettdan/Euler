# Project Euler: Problem 1
# Multiples of 3 or 5
# Uses: Loops, modulo, if, print

# Problem set-up
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Set up a function called p1
def p1():

# Initialise variables x & a
# x will run through all integers from 1 to 1000
# a will keep a running total of all multiples of 3 or 5
    x=0
    a=0

# Set up a loop through 1 to 1000
    for x in range(1,1000):
# Test using modulos to see if x is a multiple of both 3 and 5, if so add x to a
        if (x % 3 == 0) or (x % 5 == 0): 
            a=a+x
# Set up a stopping criteria & print the final value of a
        if x==999:
            print(a)
        
if __name__ == "__p1__":
    p1()

# Alternative 1-liner:
# Filter function only retains elements in a sequence meeting requirement
# In this case the filter keeps only elements in 1 to 1000 that are multiples of 3 or 5
# Reduce function applies a function to all values in a list (defined in functools module)
# In this case add together elements in the list
# Both use the lambda function which allows any number of items in the list

# import functools
# print(functools.reduce(lambda x,y: x+y, filter(lambda n: n%3==0 or n%5==0, range(1000))))