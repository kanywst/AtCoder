N = int(input())

ans = 0
res = 0
for i in range(1,N+1):
    tmp = i
    cnt = 0
    while True:
        if tmp%2 == 0:
            cnt += 1
            tmp = tmp//2
        else:
            break
    if ans <= cnt:
        res = i
        ans = cnt
print(res)
