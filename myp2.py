def isperfectno():
    
    res=1
    n=int(input())
    for i in range(2,n):
       if(n%i==0):
            res=res+i
    if res==n:
        print("IT IS A PERFECT NUMNBER")
    else:
        print("IT IS NOT A PERFECT NUMBER")

isperfectno()
 
