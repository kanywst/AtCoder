x = [int(input()) for _ in range(5)]

res = []
diff = []
for i in range(5):
    tmp = 0
    if(x[i] % 10 == 0):
        tmp = (x[i] // 10) * 10
    else:
        tmp = (x[i] // 10 + 1) * 10
    res.append(tmp)
    diff.append(tmp - x[i])

print(sum(res) - max(diff))
