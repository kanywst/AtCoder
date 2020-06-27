N,Q = map(int,input().split())
res = ['0']*N
for _ in range(Q):
    l,r = map(int,input().split())
    for i in range(l-1,r):
        if res[i] == '0':
            res[i] = '1'
        else:
            res[i] = '0'
print(''.join(res))
