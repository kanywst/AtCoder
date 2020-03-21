N = int(input())
p = list(map(int,input().split()))

res = sorted(p)
cnt = 0

for i in range(N):
    if p[i] != res[i]:
        cnt += 1

if(cnt <= 2):
    print('YES')
else:
    print('NO')
