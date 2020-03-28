L,R = map(int,input().split())
m = R - L
if(m >= 2019):
    print(0)
else:
    res = []
    for i in range(L,R):
        for j in range(L+1,R+1):
            print(i,j)
            res.append((i*j)%2019)
    print(min(res))
