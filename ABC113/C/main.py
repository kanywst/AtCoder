N,M = map(int,input().split())
d=[0]*M
res = []
for i in range(M):
    P,Y = map(int,input().split())
    res.append((P,Y,i))
c=0
res.sort()
t = str(res[0][0])
for i in res:
    x = str(i[0])
    if x == t:
        c+=1
    else:
        c=1
        t = x
    d[i[2]] = (6-len(x))*'0'+x+(6-len(str(c)))*'0'+str(c)

for i in d:
    print(i)
