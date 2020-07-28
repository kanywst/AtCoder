s = input()

tmp = s[0]
res = ''
cnt=0
for i in range(len(s)):
    if tmp == s[i]:
        cnt += 1
    else:
        res += tmp + str(cnt)
        tmp = s[i]
        cnt = 1
else:
    res += tmp + str(cnt)
print(res)
