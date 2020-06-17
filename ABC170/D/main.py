N = int(input())
A = list(map(int,input().split()))

cnt = N
for i in range(N):
    for j in range(N):
        if i != j:
            if A[i]%A[j] == 0:
                cnt -= 1
                break
print(cnt)
