N = int(input())

res = 0
for i in range(11):
    if i == 10:
        tmp = 1111
    else:
        tmp = i * 111
    if tmp >= N:
        res = tmp
        break
print(res)
