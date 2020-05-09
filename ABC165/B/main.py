X = int(input())

n = 100
i = 1
while True:
    n = int(n * 0.01 + n)
    if X <= n:
         print(i)
         break
    i+=1
