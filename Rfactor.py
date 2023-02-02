import math as m
n=int(input())
sqt=int(m.sqrt(n))
i=1
def Rfactor(n):
    global i
    x=0
    if i>sqt:
        return 0
    if n%i==0:
        if i!=n//i:
            x+=n//i
        x+=i
    i+=1
    return i+Rfactor(n)


res=Rfactor(n)
print(res)
