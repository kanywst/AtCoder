import sys

N,M = map(int,input().split())
A = list(map(int,input().split()))

s = sum(A)
res = 0
tmp = sorted(A,reverse=True)

c = s/(4*M)
for i in range(M):
    if c > tmp[i]:
        print('No')
        sys.exit()
print('Yes')

'''
if s/(4*M) > res:
    print('No')
else:
    print('Yes')
'''
