N,S,T = map(int,input().split())
W = int(input())
if S<=W<=T:
    cnt = 1
else:
    cnt = 0
for _ in range(N-1):
    A = int(input())
    W += A
    if S<=W<=T:
        cnt+=1
print(cnt)
