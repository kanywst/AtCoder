from itertools import product

S = list(input())
N = int(input())

print(''.join(list(list(product(S,repeat=2))[N-1])))
