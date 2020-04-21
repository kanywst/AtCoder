N = int(input())
A = list(map(int,input().split()))

'''
A = sorted([i-k-1 for k,i in enumerate(A)])
b = A[N//2]
print(sum(abs(i-b) for i in A))
'''
for i in range(N):
    A[i] = A[i]-i-1
A.sort()
b = A[N//2]
print(sum(list(map(lambda x:abs(x-b),A))))
