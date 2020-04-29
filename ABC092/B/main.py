N = int(input())
D,X = map(int,input().split())
A = [int(input()) for _ in range(N)]

res = 0
for i in range(N):
    res += len(list(range(1,D+1,A[i])))
print(res+X)
