N = int(input())
A = list(map(int,input().split()))

cal = 0.0
for i in range(N):
    cal += 1/A[i]

print(1/cal)
