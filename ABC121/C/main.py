N,M = map(int,input().split())

d = []
res = 0

for i in range(N):
    A,B = map(int,input().split())
    d.append((A,B))

d.sort(reverse = True)

while M:
    x = d.pop()
    n = min(M,x[1])
    res += n * x[0]
    M -= n
print(res)


'''
d = {}
for _ in range(N):
    A,B = map(int,input().split())
    d[A] = B

res = 0
cnt = 0
for i in sorted(d):
    if(d[i] <= M):
        res += d[i]*i
        M -= d[i]
    else:
        res += M * i
        break

print(res)
'''
