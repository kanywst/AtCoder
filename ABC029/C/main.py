from itertools import product

N = int(input())
abc = ['a','b','c']
res = list(map(lambda x: ''.join(x),product(abc,repeat=N)))
for i in sorted(res):
    print(i)
'''
res = []
for i in sorted(set(permutations(['a','b','c']*N,N))):
    print(''.join(list(i)))
'''
