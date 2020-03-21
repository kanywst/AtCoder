N,D = map(int,input().split())

d = D * 2 + 1
if(N%d == 0):
    print(N//d)
else:
    print(N//d+1)
