def ispoweroftwo(n):
    for x in range(n):
        if 2**x==n:
            return True
    return False

n=int(input())
print(ispoweroftwo(n))
