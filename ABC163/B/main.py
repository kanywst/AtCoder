N,M = map(int,input().split())
A = list(map(int,input().split()))

res = N - sum(A)

if res>=0:
    print(res)
else:
    print(-1)
