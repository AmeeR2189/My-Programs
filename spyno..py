def isspy(n):
    sum=0
    mul=1
    while n:
        d=n%10
        n=n//10
        sum+=d
        mul*=d
    return sum==mul




n=int(input())
res=isspy(n)
print(res)
