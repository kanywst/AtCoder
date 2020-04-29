N = int(input())
ab = []
for _ in range(N):
    a,b = map(int,input().split())
    ab.append((a,b))
cd = []
for _ in range(N):
    c,d = map(int,input().split())
    cd.append((c,d))

ab.sort(reverse=True)
cd.sort(reverse=True)

cnt = 0
for i in ab:
    for j in range(N):
        if i[0] < cd[i][0] and i[1] < cd[i][1]:
            cnt += 1
            break

print(cnt)
