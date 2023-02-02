def Magic(n):
   sum = 0
    
   while (n > 0 or sum > 9):
      if (n == 0):
         n = sum
         sum = 0
      sum = sum + n % 10
      n = int(n / 10)
      if (sum == 1):
          return 0
      else:
          return 1

n=int(input())
print(Magic(n))

