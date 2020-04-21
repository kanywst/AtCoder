N = int(input())
S = input()

res = 0
for i in range(N):
    l = S[:i]
    r = S[i:]
    cnt = 0
    for j in set(l):
        if r.count(j) > 0:
            cnt += 1
    res=max(res,cnt)
print(res)
