D,N = map(int,input().split())

c = N//100
if D == 0:
    print(N+c)
else:
    tmp = 100 ** D
    print(tmp*N+c*tmp)
