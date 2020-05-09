from itertools import permutations
import sys
N,M,Q = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(Q)]
tmp = list(range(1,M+1))
res = []
if Q == 1:
    print('1')
    sys.exit()
for i in range(1,N+1):
    res += list(map(sorted,list(permutations(tmp,i))))
res.sort()
d = []
tmp = res[0]
for i in range(1,len(res)):
    if res[i] != tmp:
         d.append(tmp)
         tmp = res[i]
point = 0
for i in d:
    ans = 0
    for j in l:
        a_i = j[0] - 1
        b_i = j[1] - 1
        c_i = j[2]
        d_i = j[3]

        if len(i) > b_i:
            if i[b_i] - i[a_i] == c_i:
                ans += d_i
    point = max(ans,point)
print(point)
