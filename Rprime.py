import math as m
i=2
def prime(n):
    global i
    if n==i:
        return True
    elif n%i==0:
        return False
    else:
        i+=1
        return prime(n)
    
n=int(input())
res=prime(n)
print(res)
