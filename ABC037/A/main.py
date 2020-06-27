l = list(map(int,input().split()))
m = sorted(l[:2])
c = l[2]
cnt = 0
for i in range(len(m)):
    tmp = c//m[i]
    c -= tmp*m[i]
    cnt += tmp
print(cnt)
