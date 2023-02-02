n=int(input())
arr=list(map(int,input().split()))
m=int(input())
for i in range(n):
    if arr[i]==m:
        print("found")
        break
else:
    print("not found")
