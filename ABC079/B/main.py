N = int(input())

res = []
for i in range(N+1):
    tmp = 0
    if i == 0:
        res.append(2)
    elif i == 1:
        res.append(1)
    else:
        tmp = res[i-1] + res[i-2]
        res.append(tmp)
print(res[-1])
