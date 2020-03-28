N,L = map(int,input().split())

l = [0] * N
for i in range(N):
    l[i] = L + i

ans = sum(l)
res = 10 ** 9
d = 0
for i in range(N):
    tmp = l[:i] + l[i+1:]
    solve = sum(tmp)
    c = abs(ans - solve)

    if(res > c):
        res = c
        d = solve

print(d)
