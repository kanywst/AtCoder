N,K = map(int,input().split())
res = [0] * N
for i in range(K):
    d = int(input())
    A = list(map(int,input().split()))
    for j in A:
        res[j-1] +=1
print(res.count(0))
