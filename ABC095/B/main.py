N,X = map(int,input().split())
m = [int(input()) for _ in range(N)]

tmp = X - sum(m)

print(tmp // min(m) + N)
