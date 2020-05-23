from collections import Counter

N = int(input())
a = list(map(int,input().split()))

c = [0 for _ in range(10**5)]

for i in a:
    c[i-1] += 1
    c[i+1] += 1
    c[i] += 1
print(max(c))

'''
res = 0
for i in a:
    cnt = 0
    cnt += a.count(i)
    cnt += a.count(i-1)
    cnt += a.count(i+1)
    res = max(res,cnt)
print(res)
'''
