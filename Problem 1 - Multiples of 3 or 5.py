# Multiples of 3 or 5
# Loops, modulo

def main():
    x=0
    a=0

    for x in range(1,1000):
        if (x % 3 == 0) or (x % 5 == 0): 
            a=a+x
        if x==999:
            print(a)
        
if __name__ == "__main__":
    main()