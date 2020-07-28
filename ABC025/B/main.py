N,A,B = map(int,input().split())
res = 0
for _ in range(N):
    s,d = input().split()
    if A<=int(d)<=B:
        d = int(d)
    elif A > int(d):
        d = A
    else:
        d = B
    if s == 'East':
        res += int(d)
    else:
        res -= int(d)
if res > 0:
    print('East',res)
elif res < 0:
    print('West',abs(res))
else:
    print(res)
