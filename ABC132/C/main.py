N = int(input())
d = list(map(int,input().split()))

lim = len(d) // 2 - 1
res = sorted(d)

print(res[lim+1] - res[lim])
