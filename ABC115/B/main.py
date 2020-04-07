N = int(input())
p = list(int(input()) for _ in range(N))

tmp = sorted(p,reverse=True)
print(tmp[0]//2 + sum(tmp[1:]))
