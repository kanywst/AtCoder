S = input()

cnt = 0
res = 0
for i in S:
    if('A' == i or 'T' == i  or 'C' == i or 'G' == i):
        cnt += 1
    else:
        cnt = 0
    res = max(res,cnt)
print(res)
