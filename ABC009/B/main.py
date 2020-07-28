N = int(input())
A = sorted(list(set([int(input()) for _ in range(N)])),reverse=True)
print(A[1])
