import sys

K = int(input())
A,B = map(int,input().split())

tmp = A//K

for i in range(1000):
    t = (tmp+i) * K
    if A<= t <= B:
        print('OK')
        sys.exit()
    if t > B:
        break
print('NG')
