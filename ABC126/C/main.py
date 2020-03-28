N,K = map(int,input().split())

ans = 0
for i in range(1,N+1):
    cnt = 0
    res = i
    while True:
        if res < K:
            res = res * 2
            cnt += 1
        if res >= K:
            break
    ans += (1/N) * pow(1/2,cnt)
print(ans)
