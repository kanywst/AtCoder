N,T = map(int,input().split())
A = [int(input()) for _ in range(N)]

l=A[0]
r=A[0]
res=0
for i in range(1,N):
    if r+T > A[i]:
        r=A[i]
    else:
        res+=(r+T-l)
        l = A[i]
        r = A[i]
else:
    res += r+T-l

print(res)
