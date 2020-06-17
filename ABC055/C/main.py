N,M = map(int,input().split())

if N*2>=M:
    print(M//2)
else:
    tmp = M - N*2
    print(tmp//4+N)
