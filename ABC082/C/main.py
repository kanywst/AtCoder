from collections import Counter

N = int(input())
a = list(map(int,input().split()))

c = Counter(a)
cnt = 0
for key,value in Counter(a).items():
    if key < value:
        cnt += value - key
    if key > value:
        cnt += value
print(cnt)
