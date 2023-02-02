def Rmul(a,b):
    if a==1:
        return b
    if a%2:
        return b+Rmul(a//2,b*2)
    else:
        return Rmul(a//2,b*2)


a,b=map(int,input().split())
res=Rmul(a,b)
print(res)
