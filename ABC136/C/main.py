import sys

N = int(input())
H = list(map(int,input().split()))

for i in range(1,N-1):
    if not(H[i-1] <= H[i] <= H[i+1]):
        tmp = H[i] - 1
        if not(H[i-1] <= tmp <= H[i+1]):
            print('No')
            sys.exit()
        H[i] = tmp
    if H[i-1] < H[i]:
        print('A')
        H[i] -= 1
print('Yes')
