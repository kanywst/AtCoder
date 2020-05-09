N = int(input())
a = sorted(list(map(int,input().split())),reverse=True)
res = 0
for i in range(N):
    if i % 2 == 0:
        res += a[i]
    else:
        res -= a[i]
print(res)
