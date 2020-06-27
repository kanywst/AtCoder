import copy
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
res = []
tmp = copy.copy(A)
for _ in range(Q):
    B,C = map(int,input().split())
    for i in range(N):
        if tmp[i] == B:
            tmp[i] = C
    else:
        res.append(sum(tmp))
for i in res:
    print(i)
