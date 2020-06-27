N = int(input())
a = list(map(int,input().split()))
d = {}
for i in range(N):
    d[i] = a[i]
for i in sorted(d.items(),key=lambda x:x[1],reverse=True):
    print(i[0]+1)
