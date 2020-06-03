N = int(input())
a = list(map(int,input().split()))

Q = [x for x in a if x%4==0]
W = [x for x in a if x%4==2]

print(Q)
print(W)

if len(Q)>=n//2:
    print('Yes')
else:
    if len(W)>=n-len(Q)*2:
        print('Yes')
    else:
        print('No')
