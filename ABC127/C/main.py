N,M = map(int,input().split())

L_list = []
R_list = []

for i in range(M):
    L,R = map(int,input().split())
    L_list.append(L)
    R_list.append(R)

l = max(L_list)
r = min(R_list)

if(l > r):
    print(0)
else:
    print(r-l+1)
