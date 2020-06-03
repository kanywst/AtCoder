import sys
N = int(input())
A = sorted(list(map(int,input().split())))

res = 1
for i in A:
    if res > 10**18:
        print(-1)
        sys.exit()
    res *= i

if res > 10**18:
    print(-1)
else:
    print(res)
