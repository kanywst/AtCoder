N,A,B = map(int,input().split())

cnt = 0
for i in range(1,N+1):
    n = sum(list(map(int,list(str(i)))))
    if A<=n<=B:
        cnt += i
print(cnt)
