# Project Euler: Problem 3
# Largest prime factor
# Uses: Loops, modulo, if, print, square root, logs
# Import: math package

# Problem set-up
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Import the math package
import math

# Set up a function called p3
def p3():

# x= original value
# y= remaining value
# b= log (base 2) of x (sets upper bound for later loop)
# c= square root of y (sets upper bound for later loop)
# a= current highest prime factor    
    x=600851475143
    y=x
    b=math.ceil(math.log2(x))
    c=math.ceil(math.sqrt(y))
    a=10

# Set up a loop from 1 to log(x)
    for j in range(1,b):
# if criteria checking if y is even, if so halves and sets current highest prime as 2
        if (y % 2 == 0): 
            y=y/2
            a=2

# Set up a loop from 3 to square root of original number
    for i in range(3,c):
# Checks each value to see if if perfectly divides the remaining value, if so divide and set this value as highest prime
        if (y % i == 0):
            y=y/i
            a=i

# Print results    
    print(max(a,y))

if __name__ == "__p3__":
    p3()
