N = int(input())
d = []
res = 0
for _ in range(N):
    x,y,h = map(int,input().split())
    d.append((x,y,h))
    ans = 0
    for cx in range(0,101):
        for cy in range(0,101):
            #print(cx,cy)
            ans = max(h - abs(x-cx) - abs(y-cy),0)
            #if ans>0:
            #    print(ans)
    res=max(res,ans)
    print(res)
print(d)
