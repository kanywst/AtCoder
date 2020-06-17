X,Y = map(int,input().split())

a = 4*X-Y
b = (4-2)
tmp = a//b
if a%b == 0 and tmp >=0 and (X-tmp)>=0:
    print('Yes')
else:
    print('No')
