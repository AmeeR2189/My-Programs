def thief(m,n):
    if(m%2==0):
        a=m//2
        return a*n
    else:
        a=(m//2)+1
        return a*n
    

m,n=map(int,input().split())
print(thief(m,n))
