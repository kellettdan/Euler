# Largest palindromic product
# Loops, recursion

def main():

    maxk=0
    for j in range(100,1000):
        for i in range(100,1000):
            k=i*j
            rev_k = 0
            while (k>0):
                remainder = k % 10
                rev_k = (rev_k * 10) + remainder
                k = k // 10            
            if rev_k==i*j and rev_k>maxk:
                maxk=rev_k
    print(maxk)

if __name__ == "__main__":
    main()