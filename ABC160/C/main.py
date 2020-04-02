K,N = map(int,input().split())
A = list(map(int,input().split()))

#res = 0
if 0 in A:
    A.remove(0)

print(abs(max(A) - min(A)))
'''
ans = 10 ** 10
for i in range(N):
    t0 = A[0]
    A.remove(t0)
    A.append(t0)
#    print(A)
    for j in range(N-1):
        if(A[j] == 0):
            res += 0
        else:
            res += abs(A[j] - A[j+1])
    if(ans > res):
        ans = res
    res = 0
print(ans)
'''
