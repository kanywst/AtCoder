import sys
a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in a:
    if i in b:
        print('YES')
        sys.exit()
print('NO')
