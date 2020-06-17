import sys
X,N = map(int,input().split())
if N == 0:
    print(X)
    sys.exit()
p = sorted(list(map(int,input().split())))

c = 1
while True:
    if X in p:
        if not((X-c) in p):
            print(X-c)
            break
        if not((X+c) in p):
            print(X+c)
            break
        c += 1  
    else:
        print(X)
        break
'''
d = list(range(p[0],p[N-1]))
ans = []
for i in d:
    if not(i in p):
        ans.append(i)
res = 1e+9
c = 0
for i in ans:
    tmp = abs(X-i)
    if tmp < res:
        res = tmp
        c = i
print(c)
'''
