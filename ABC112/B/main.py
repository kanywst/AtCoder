import sys

N,T = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(N)]

for i in sorted(d):
    if i[1] <= T:
        print(i[0])
        sys.exit()
else:
    print('TLE')
