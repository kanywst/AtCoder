N,Q = map(int,input().split())
res = [0]*N
for _ in range(Q):
    L,R,T = map(int,input().split())
    for i in range(L-1,R):
        res[i] = T
for i in res:
    print(i)
