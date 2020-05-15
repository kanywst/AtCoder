from itertools import permutations

N,M,X = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(N)]

r = list(permutations(range(N),N))

ans = 1e+9
for i in r:
    res = 0
    tmp = l[i[0]][1:]
    for j in i[1:]:
        C = l[j][0]
        A = l[j][1:]
        tmp = [x+y for (x,y) in zip(A,tmp)]
        print(tmp)
        res += C
        if tmp != [] and min(tmp) >= X:
            ans = min(res,ans)
            break
    tmp = []
    res = 0
print(ans)


'''
d = {}
for i in l:
    C = i[0]
    A = i[1:]
    d[str(sum(A))] = C
tmp = sorted(map(int,d.keys()),reverse=True)

s = []
for i in tmp:
    for j in range(N):
        if d[str(i)] == l[j][0]:
            s.append(l[j])
print(s)

res = s[0][0]
res_lst = s[0][1:]

for i in range(1,N-1):
    C = s[i][0]
    A = s[i][1:]

    tmp = [x+y for (x,y) in zip(A,res_lst)]
    res += C
    if X <= min(tmp):
        break
    res_lst = tmp
else:
    res = -1
print(res)
'''
