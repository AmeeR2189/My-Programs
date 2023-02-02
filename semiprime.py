import math as M
def isprime(n):
    sq=int(M.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
def issemiprime(n):
    sq=int(M.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0 and isprime(i) and isprime(n//i):
            return True
    return False



n=int(input())
res=issemiprime(n)
print(res)
