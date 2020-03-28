import itertools
#from collections import Counter

N = int(input())
A = list(map(int,input().split()))

#c = Counter(A)
print(c)
for i in range(N):
    tmp = A[:i] + A[i+1:]

    res = 0
    for j in set(tmp):
        l = tmp.count(j)
        res += len(list(itertools.combinations([0]*l,2)))
    print(res)
