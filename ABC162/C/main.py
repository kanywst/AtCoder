from fractions import gcd

K = int(input())

res = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        tmp = gcd(i,j)
        for k in range(1,K+1):
            res += gcd(tmp,k)
print(res)
