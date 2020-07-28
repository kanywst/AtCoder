from collections import Counter

n = int(input())
s = [input() for _ in range(n)]

res = 0
tmp = 0
for key,value in Counter(s).items():
    if tmp < value:
        tmp = value
        res = key
print(res)
