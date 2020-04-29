N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    tmp = [0] + A[:i] + A[i+1:] + [0]

    res = 0
    for j in range(len(tmp)-1):
        res += abs(tmp[j+1] - tmp[j])
        print(res)
