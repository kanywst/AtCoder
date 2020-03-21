import copy

N = int(input())
A = [int(input()) for _ in range(N)]

res = sorted(A,reverse=True)
for i in range(N):
    if A[i] == res[0]:
        print(res[1])
    else:
        print(res[0])
    #tmp = copy.deepcopy(A)
    #tmp.remove(A[i])
    #print(max(tmp))
