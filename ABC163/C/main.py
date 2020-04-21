N = int(input())
A = list(map(int,input().split()))

res = [0]*N

for i in range(N-1):
    res[A[i]-1] += 1

for i in res:
    print(i)
