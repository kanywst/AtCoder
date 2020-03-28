n = int(input())
p = list(map(int,input().split()))

cnt = 0
for i in range(n-2):
    tmp = p[i:i+3]
    ma = max(tmp)
    mi = min(tmp)
    if(tmp[1] != ma and tmp[1] != mi):
        cnt += 1
print(cnt)
