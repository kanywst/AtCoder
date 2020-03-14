N = int(input())
H = list(map(int,input().split()))

ans = 0
tmp = 0

for i in range(N-1):
    if(H[i] < H[i+1]):
        #ans = max(ans,tmp)
        tmp = 0
    else:
        tmp += 1
    ans = max(ans,tmp)

print(ans)

'''
maximum = 0
cnt = 0

for i in range(len(H)):
    k = H[i]
    res = H[i+1:]
    for j in res:
        if(j <= k):
            cnt += 1
            k = j
        else:
            break
        maximum = max(maximum,cnt)
        #if(max < cnt):
        #    max = cnt
    cnt = 0

print(maximum)
'''
