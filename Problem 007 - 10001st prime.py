# Project Euler: Problem 7
# 10001st prime
# Uses: Loops, modulo, if, print

# Problem set-up
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# Set up a function called p7
def p7(terms):

# Initialise pnum as the current prime number (starting at 2 as the first prime)
# Initialise pcnt as the nth prime (starting at 1 as 2 is the 1st prime) 
    pnum=2
    pcnt=1

# Loop from 3 up to 1 million, moving up by 2 each time
    for i in range(3,1000000,2):
        for j in range(2,i):
# Test if i is divisible by all numbers below
            if(i % j ==0):
                break
        else:
# If prime found increment pcnt by 1 & set new highest prime as pnum
            pnum=i
            pcnt=pcnt+1
# Once pcnt equals the desired nth prime then break and print
            if pcnt==terms:
                break
    print(pnum)
        
p7(10001)