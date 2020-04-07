from itertools import combinations

N,K = map(int,input().split())
h = [int(input()) for _ in range(N)]

'''
res = 10**10
for i in combinations(h,K):
    tmp = max(i) - min(i)
    res = min(res,tmp)
'''

d = sorted(h)
res = 1e+9
for i in range(N-K+1):
    res = min(res,d[i+K-1] - d[i])
print(res)
