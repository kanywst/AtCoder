N,M = map(int,input().split())
d = {}
for i in range(M):
    a,b = map(int,input().split())
    if a in d.keys():
        d[a].append(b)
    else:
        d[a] = [b]

flag = False
for i in d[1]:
    if i in d.keys():
        for j in d[i]:
            if j == N:
                flag = True
                break
        if flag:
            break
if flag:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
