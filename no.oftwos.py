def twos(n):
    c=0
    for i in arr:
        if(i==2):
            c+=1
    return c

n=int(input())
arr=list(map(int,input().split()))
print(twos(n))
