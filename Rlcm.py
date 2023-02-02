i=2
def Rlcm(a,b):
    global i
    r=1
    if a<i or b<i:
        return a*b
    if a%i==0 and b%i==0:
        a=a//i
        b=b//i
        r=i
    else:
        i+=1
    return r*Rlcm(a,b)



a,b=map(int,input().split())
res=Rlcm(a,b)
print(res)
