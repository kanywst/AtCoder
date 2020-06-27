N = int(input())

ans = ''

while True:
    N -= 1
    N,mod = N//26,N%26
    ans += chr(ord('a')+mod)
    if N ==0:
        break
print(ans[::-1])
'''
tmp = N
cnt=1
if N%26 == 0:
    while True:
        if N == 26:
            cnt = 1
            break
        elif tmp//26 < 28:
            cnt += 1
            break
        else:
            tmp = tmp//26
            cnt += 1
else:
    while True:
        if tmp//26 < 1:
            break
        else:
            tmp = tmp//26
            cnt += 1
res = ''
next = N
for i in range(cnt):
    tmp = next%26
    next = next//26
    if tmp == 0:
        res += 'z'
        next -= 1
    elif tmp+96>122:
        res += chr((tmp+96)-26)
    elif tmp+96<97:
        res += chr((tmp+96)+26)
    else:
        res += chr(tmp+96)
print(res[::-1])
'''
