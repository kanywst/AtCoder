N,K,Q = map(int,input().split())
A = list(input() for _ in range(Q))
points = [K for _ in range(N)]

points = list(map(lambda x:x-Q,points))

for i in A:
    points[int(i)-1] += 1

for i in points:
    if(i > 0):
        print('Yes')
    else:
        print('No')
