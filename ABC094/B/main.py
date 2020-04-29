N,M,X = map(int,input().split())
A = list(map(int,input().split()))

ans0 = 0
ans1 = 0
for i in range(0,X):
    if i in A:
        ans0 += 1

for i in range(X,N+1):
    if i in A:
        ans1 += 1

print(min(ans0,ans1))
