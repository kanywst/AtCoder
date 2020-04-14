A,B = map(int,input().split())

for i in range(1,4):
    tmp = A*B*i
    if tmp % 2 == 1:
        print('Yes')
        break
else:
    print('No')
