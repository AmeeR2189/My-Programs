def happyno(n):
    s=0
    while n>0:
        s+=(n%10)*(n%10)
        n//=10
    if s==1 or s==7:
        return True
    elif s==4:
        return False
    else:
        return happyno(s)
     


n=int(input())
res=happyno(n)
print(res)
