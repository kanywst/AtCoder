from collections import Counter
N = int(input())
A = [input() for _ in range(N)]

res = 0
#print(Counter(A))

c = Counter(A)
for i in c.values():
    res += i % 2
print(res)
