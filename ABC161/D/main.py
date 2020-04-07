import sys

K = int(input())

if K<=9:
    print(K)
    sys.exit()

c = 10
res = 10
d = 10

while True:
    if(c == K):
        break
    tmp = list(str(d))
    for i in range(len(tmp)-1):
        if abs(int(tmp[i]) - int(tmp[i-1])) > 1:
            break
        d += 1
    else:
        res = d
        c += 1
print(res)

'''
if(K <= 9):
    print(K)
    sys.exit()

tmp = (K - 9)
d = K // 9 + 1
print("d:",d)

if tmp %(d+1) == 0:
    div = tmp//(d+1)
    mod = (d+1)
else:
    div = tmp//(d+1) + 1
    mod = tmp%(d+1)
#mod = tmp%3

print("div:",div)
print("mod:",mod)

dig = 10 ** len(str(div))
print("dig:",dig)
base = div * dig + (div-1)
print(base)
print(base + mod -1)
'''
