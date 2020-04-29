A,B,K = map(int,input().split())

l = list(range(A,B+1))
res = set(l[:K] + l[-K:])
'''
l = list(range(A,B+1))
res = []
for i in range(len(l)):
    if i < K:
        res.append(l[i])
    if B-A+1-K <= i:
        res.append(l[i])

'''
for i in sorted(set(res)):
    print(i)
