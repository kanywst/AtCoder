from itertools import combinations
l = map(int,input().split())
tmp = sorted(list(map(sum,combinations(l,3))))
print(tmp[-3])
