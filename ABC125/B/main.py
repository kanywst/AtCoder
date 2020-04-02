N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

tmp = []
for i in range(N):
    tmp.append(V[i] - C[i])

res = 0
for i in range(N):
    if(tmp[i] > 0):
        res += tmp[i]
print(res)
