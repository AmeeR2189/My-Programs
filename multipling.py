def multiply(a,b):
    mul=0
    while a:
        if a%2:
            mul=mul+b
        a=a//2
        b=b*2
    return mul


a,b=map(int,input().split())
res=multiply(a,b)
print(res)
