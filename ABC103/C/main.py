from fractions import gcd
from functools import reduce

def lcm(x, y):
    return (x * y) // gcd(x, y)

N = int(input())
a = list(map(int,input().split()))

res = 0
tmp = reduce(lcm,a)-1
for i in a:
    res += tmp % i
print(res)
