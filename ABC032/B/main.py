s = input()
k = int(input())
res = []
for i in range(len(s)-(k-1)):
    tmp = s[i:i+k]
    if not(tmp in res):
        res.append(tmp)
print(len(res))
