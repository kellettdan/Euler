# Special Pythagorean triplet

import math

def p9(x):

    for i in range(1,x):
        for j in range(1,x):
            for k in range(1,x):
                if i**2 + j**2 == k**2:
                    if i + j + k == x:
                        print(i*j*k)
        
p9(1000)