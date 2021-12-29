# Smallest multiple

import math

def main():

    max_val = math.factorial(20) + 1
    min_j = max_val

    for j in range(9699690,max_val):
        k=0
        for i in range(1,21):
            if (j % i == 0):
                k=k+1
        if k==20:
            min_j=j
            break
    print(min_j)

if __name__ == "__main__":
    main()