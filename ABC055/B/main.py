N = int(input())

res = 1
for i in range(1,N+1):
    res = (res*i)%(10**9+7)
print(res)
