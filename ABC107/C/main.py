N,K = map(int,input().split())
x = list(map(int,input().split()))

res = 1e+9
for i in range(N-K+1):
    if abs(x[i]) <= abs(x[i+K-1]):
        res = min(res,abs(x[i]) + abs(x[i+K-1] - x[i]))
    else:
        res = min(res,abs(x[i+K-1]) + abs(x[i+K-1] - x[i]))
print(res)
