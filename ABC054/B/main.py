N,M = map(int,input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

def comp(x,y):
    for i in range(M):
        for j in range(M):
            if A[x+i][y+j] != B[i][j]:
                return False
    return True
flag = False
for i in range(N-M+1):
    for j in range(N-M+1):
        if comp(i,j):
            flag = True
            break
if flag:
    print('Yes')
else:
    print('No')
'''
cnt = 0
if A < B:
    print('No')
    sys.exit()
else:
    for i in range(N):
        for j in range(M):
            if B[j] in A[i]:
                cnt+=1
                flag = True
            else:
                cnt = 0
                flag = False
        if cnt == M:
            break
if flag:
    print('Yes')
else:
    print('No')
'''
