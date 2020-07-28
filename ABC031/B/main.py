L,H = map(int,input().split())
N = int(input())
res = []
for _ in range(N):
    A = int(input())
    if L<=A<=H:
        res.append(0)
    elif A > H:
        res.append(-1)
    elif L > A:
        res.append(L-A)
for i in res:
    print(i)
