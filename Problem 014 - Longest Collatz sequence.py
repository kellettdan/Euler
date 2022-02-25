# Project Euler: Problem 14
# Special Longest Collatz sequence
# Uses: 

# Problem set-up
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# Once the chain starts the terms are allowed to go above one million.

# Set up a function called p14 where cap is the maximum value to start the search from
def p14(cap):

# Initialise max as the maximum number of terms in a sequence found so far, starting with 1
# Initialise maxnum as the number with the most terms in a sequence found so far, starting with 1
    max=1
    maxnum=1
    
# Loop through 1 to cap
    for i in range(1,cap):
# Initialise currterms as a counter for the current terms, initialised at 1            
# Initialise currnum as a counter for the current number, initialised at 1            
        currterms=1
        currnum=i
        print(i,maxnum)
        while currnum > 1:

            if (currnum % 2 ==0):
                currnum = currnum / 2
                currterms = currterms + 1
            else:
                currnum = currnum * 3 + 1
                currterms = currterms + 1
        if currterms > max:
            max = currterms
            maxnum=i

# Print final sum
    print(maxnum)
        
p14(1000000)