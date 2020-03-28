from itertools import combinations

l = list(map(int,input().split()))
tmp = list(combinations(l,2))

res = 10**10
for i in tmp:
    m = sum(i)
    if res > m:
        res = m

print(res)
