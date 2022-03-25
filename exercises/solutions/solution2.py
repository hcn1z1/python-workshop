m = float(input("Enter the distance between two walls"))
n = float(input("Enter the speed of the ball"))

M=m
N=n 
x=0
k=0
if (n<m):
    k=n
    print("x {} et k = {}".format(x,k))
elif(n>m):
    while True:
        n=n-1
        if (n<1):
            m = m-1
            if (m==0):
                m = M 
                x = x+1
                if ((n-2.5)<=0):
                    if(x%2==0):
                        k= (N-((x-1)*2.5)-n)%M 
                    else:
                        k = M - (N-((x-1)*2.5)-n)%M
                    print("x = {} et k = {} ".format(x,k))
                    break
                else:
                    n = n-2.5
            else:
                if(m-n==0):
                    x=x+1
                    if(x%2==0):
                        k= (N-(x-1)*2.5)%M 
                    else:
                        k = M - (N-(x-1)*2.5)%M 
                else:
                    if(x%2==0):
                        k= (N-x*2.5)%M
                    else:
                        k = M - (N-x*2.5)%M
                print("x = {} et k = {} ".format(x,k))
                break


        m=m-1
        if (m==0):
            m = M 
            x = x+1
            if ((n-2.5)<=0):
                if(x%2==0):
                    k= (N-((x-1)*2.5)-n)%M 
                else:
                    k = M - (N-((x-1)*2.5)-n)%M
                print("x = {} et k = {} ".format(x,k))
                break
            else:
                n = n-2.5
            
else:
    k=n
    print("x= 1 et k = {}".format(n))

