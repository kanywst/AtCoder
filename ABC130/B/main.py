N,X = map(int,input().split())
L = list(map(int,input().split()))

tmp = 0
cnt = 1

for i in range(N):
    tmp += L[i]

    if(tmp <= X):
        cnt += 1
print(cnt)
