from collections import Counter
N = int(input())
s = sorted([input() for _ in range(N)])
M = int(input())
t = sorted([input() for _ in range(M)])

d = {}
for val,cnt in Counter(s).items():
    d[val] = cnt

for val,cnt in Counter(t).items():
    if val in d:
        d[val] -= cnt
print(max(max(d.values()),0))
