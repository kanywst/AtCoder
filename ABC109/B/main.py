import sys
N = int(input())
W = [input() for _ in range(N)]

if len(set(W)) != len(W):
    print('No')
    sys.exit()

for i in range(N-1):
    if W[i][-1] != W[i+1][0]:
        print('No')
        break
else:
    print('Yes')
