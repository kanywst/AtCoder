N = input()

tmp = sum(map(int,list(N)))

if int(N)%tmp == 0:
    print('Yes')
else:
    print('No')
