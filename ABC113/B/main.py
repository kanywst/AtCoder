N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

res = 1e+9
c = 0
for i in range(N):
    t = T - H[i] * 0.006
    tmp = abs(t - A)
    if res > tmp:
        res = tmp
        c = i
print(c+1)
