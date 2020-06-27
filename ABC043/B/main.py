s = input()

res = ''
for i in s:
    if i=='B':
        res = res[:-1]
    else:
        res += i
print(res)
