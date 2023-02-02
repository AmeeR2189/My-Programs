def arrequal(a,b):
    for i in a:
        if(a.count(i)!=b.count(i)):
            return 0
            
        else:
            return 1

a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(arrequal(a,b))
