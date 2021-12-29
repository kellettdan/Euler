# Sum square difference
# Loops, squaring

import math

def p6(terms):
    ssq=0
    sqs=0
    for x in range(1,terms+1):
        ssq=ssq+(x**2)
    for y in range(1,terms+1):
        sqs=sqs+y
    sqs=sqs**2
    diff=sqs-ssq
    print(diff)
        
p6(100)