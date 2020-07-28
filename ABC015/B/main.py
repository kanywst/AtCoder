import math
N=int(input())
A = sorted(list(map(int,input().split())))
A = A[A.count(0):]
print(math.ceil(sum(A)/len(A)))
