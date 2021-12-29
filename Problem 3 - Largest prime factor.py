# Largest prime factor
# Loops
import math
# x= original value
# y= remaining value
# a= current highest prime factor

def main():
    x=600851475143
    y=x
    b=math.ceil(math.log2(x))
    c=math.ceil(math.sqrt(y))
    a=10

    for j in range(1,b):
        if (y % 2 == 0): 
            y=y/2
            a=2

    for i in range(3,c):
        if (y % i == 0):
            y=y/i
            a=i
    
    print(max(a,y))

if __name__ == "__main__":
    main()
