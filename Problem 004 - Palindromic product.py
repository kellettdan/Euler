# Project Euler: Problem 4
# Largest palindromic product
# Uses: Loops, modulo, if, print, recursion

# Problem set-up
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Set up a function called p4
def p4():

# Intialise maxk to 0, this will be the maximum solution found
    maxk=0
# Set up 2 loops (i and j) to go through all 3-digit numbers
    for j in range(100,1000):
        for i in range(100,1000):
# Multiply the numbers together to get k
            k=i*j
# Initialise rev-k - you will use recursion to create rev_k as the reverse of k using modulos
            rev_k = 0
            while (k>0):
                remainder = k % 10
                rev_k = (rev_k * 10) + remainder
                k = k // 10            
# Check if rev_k equals k (a palindronic number). If so, set this as the new maxk
            if rev_k==i*j and rev_k>maxk:
                maxk=rev_k
# Print solution
    print(maxk)

if __name__ == "__p4__":
    p4()