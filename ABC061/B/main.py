N,M = map(int,input().split())
res = {}
for i in range(1,N+1):
    res[i] = 0
for _ in range(M):
    a,b = map(int,input().split())
    res[a] += 1
    res[b] += 1
    '''
    if a in res.keys():
        res[a] += 1
    else:
        res[a] = 1
    if b in res.keys():
        res[b] += 1
    else:
        res[b] = 1
    '''
for key in sorted(res.keys()):
    print(res[key])
