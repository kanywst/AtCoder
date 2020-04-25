l = list(map(int,input().split()))
K = int(input())

for i in range(K):
    l = sorted(l,reverse=True)
    l[0] = l[0] * 2
print(sum(l)) 
