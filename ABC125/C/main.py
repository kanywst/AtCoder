from fractions import gcd

N = int(input())
A = list(map(int,input().split()))
'''
res = 0
for i in range(N):
    tmp = A[i+1:] + A[:i]
    ans = tmp[0]
    for i in range(1,N-1):
        ans = gcd(ans,tmp[i])
    res = max(ans,res)
print(res)
'''

L = [0] * (N+1)
R = [0] * (N+1)

for i in range(N):
    L[i+1] = gcd(L[i],A[i])
    R[N-i-1] = gcd(R[N-i],A[N-i-1])
ans = 0
for i in range(N):
    ans = max(ans,gcd(L[i],R[i+1]))

print(ans)
