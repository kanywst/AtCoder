N,T = map(int,input().split())
t = list(map(int,input().split()))

res = 0
for i in t:
    if i < T:
        res += i
    else:
        res += T
print(res+T)
