n = [int(input()) for _ in range(3)]
tmp = sorted(n,reverse=True)
res = {}
for i in range(3):
    res[tmp[i]] = i+1
for i in n:
    print(res[i])
