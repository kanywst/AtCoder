import copy
N = int(input())
s = []
for _ in range(N):
    s.append(input())
res = []
for i in range(N):
    tmp =''
    for j in range(N):
        tmp += s[j][i]
    else:
        res.append(tmp[::-1])
for i in res:
    print(i)
