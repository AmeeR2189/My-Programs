def lcm(a,b):
    i=2
    r=1
    while a>=i and b>=i:
        if a%i==0 and b%i==0:
            a=a//i
            b=b//i
            r=r*i
        else:
            i+=1
    return r*a*b
            



a,b=map(int,input().split())
res=lcm(a,b)
print(res)
