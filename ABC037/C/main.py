N,K = map(int,input().split())
a = list(map(int,input().split()))
res = 0
for i in range(N-K+1):
    res += sum(a[i:K+i])
print(res)
