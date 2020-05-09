from itertools import combinations
from collections import Counter
N = int(input())
S = [input() for _ in range(N)]

d = []
MARCH = list('MARCH')
for i in S:
    for j in MARCH:
        if i[0] == j:
            d.append(j)
print(Counter(d))
if Counter(d) != Counter():
    res = 1
else:
    res = 0
for i in Counter(d).values():
    res *= i
print(res)
