import sys

N,M = map(int,input().split())
X = sorted(list(map(int,input().split())))

if N >= M:
    print(0)
    sys.exit()
    
s= [0]*(M-1)
for i in range(M-1):
    s[i] = X[i+1] - X[i]
s.sort(reverse=True)
res = sum(s)
if M == 1:
    res = 0
else:
    for i in range(N-1):
        res -= s[i]
print(res)
