N,M = map(int,input().split())
a = [int(input()) for _ in range(M)]

MOD = 1000000007

d = [0] * (N+1)
OK = [True]*(N+1)
d[0] = 1

for i in range(M):
    OK[a[i]] = False

#print(OK)

if(OK[1]):
    d[1] = 1
else:
    d[1] = 0

for i in range(2,N+1):
    if(OK[i-1]):
        d[i] += d[i-1]
    if(OK[i-2]):
        d[i] += d[i-2]
    d[i] %= MOD
    '''
    if(i in a):
        d[i] = 0
    else:
        d[i] = d[i-1] + d[i-2]
    d[i] %= MOD
    '''

print(d[-1])
