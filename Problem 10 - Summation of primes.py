# Summation of primes

def p10(cap):
    
    psum=2
    plist=[2]

    for i in range(3,cap,2):
        for j in plist:
            if(i % j ==0):
                break
        else:
            psum=psum+i
            plist.append(i)
            print(i,psum)
    print(psum)
        
p10(2000000)