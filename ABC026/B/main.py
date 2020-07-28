import math
N = int(input())
R = sorted([int(input()) for _ in range(N)],reverse=True)

res = 0
for i in range(N):
    if i%2==0:
        res += R[i]**2
    else:
        res -= R[i]**2
print(res*math.pi)
