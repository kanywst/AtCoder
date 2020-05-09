N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))

res = 0
for i in range(N):
    tmp1 = sum(A1[:N-i])
    tmp2 = sum(A2[-1-i:])
    res  = max(res,tmp1+tmp2)
print(res)
