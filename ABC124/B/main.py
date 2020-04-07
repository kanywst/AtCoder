N,M = map(int,input().split())
#l = [list(map(int,input().split())) for _ in range(N)]

K = []
A = []
for _ in range(N):
    tmp = list(map(int,input().split()))
    K.append(tmp[0])
    A += tmp[1:]
    #A.append(tmp[1:])
#print(sorted(A))
cnt = 0
for i in range(1,M+1):
    #print(A.count(i))
    if(A.count(i) == N):
        cnt += 1
print(cnt)
