N=int(input())
A=[int(input()) for _ in range(N)]
cnt = 0
print(len(A)-len(set(A)))
'''
for i in range(N):
    if A[i] in A[i+1:]:
        cnt+=1
print(cnt)
'''
