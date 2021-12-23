# 10001st prime

def p7(terms):
    
    pnum=2
    pcnt=1

    for i in range(3,1000000,2):
        for j in range(2,i):
            if(i % j ==0):
                break
        else:
            pnum=i
            pcnt=pcnt+1
            if pcnt==terms:
                break
    print(pnum)
        
p7(10001)