N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

res = 0
for i in range(N):
    if(A[i] < B[i]):
        res += A[i]
        tmp = B[i] - A[i]
        A[i] = 0
        if(tmp < 0):
            tmp = 0
        if(A[i+1] < tmp):
            res += A[i+1]
            A[i+1]=0
        else:
            res += tmp
            A[i+1] -= tmp
    else:
        res += B[i]
        A[i] = 0
print(res)
