# Fibonacci
# Loops, modulo, retaining values

def main():
    x=1
    y=1
    z=0
    p=1
    a=0

    while x < 4000001:
        if (p % 3 == 2): 
            a=a+x
            print(a)
        p=p+1
        z=x
        x=x+y
        y=z
        

if __name__ == "__main__":
    main()