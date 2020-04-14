from fractions import gcd
from functools import reduce
N,X = map(int,input().split())
x = list(map(int,input().split()))
res = list(map(lambda x: abs(x-X),sorted(x)))
print(reduce(gcd,res))
