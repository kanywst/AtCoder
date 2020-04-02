N,M,C = map(int,input().split())
B = list(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
for a in A:
    res = 0
    for i in zip(a,B):
        res += i[0] * i[1]
    res += C
    if(res > 0):
        cnt += 1
print(cnt)
