# Project Euler: Problem 10
# Special Summation of primes
# Uses: Loops, modulo, if, print

# Problem set-up
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Set up a function called p10 where cap maximum value to search over
def p10(cap):

# Initialise psum as the ongoing sum of primes, starting with 2
# Initialise plist as a ist holding all primes founds    
    psum=2
    plist=[2]

# Loop through 3 to cap incrementing by 2
    for i in range(3,cap,2):
        for j in plist:
# Test each value of i by dividing by the each element in the list of primes
            if(i % j ==0):
                break
        else:
# If new prime found add to list and add to sum
            psum=psum+i
            plist.append(i)
            print(i,psum)
# Print final sum
    print(psum)
        
p10(2000000)