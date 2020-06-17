N,M = map(int,input().split())
s = []
for _ in range(N):
    a,b = map(int,input().split())
    s.append((a,b))
check = []
for _ in range(M):
    c,d = map(int,input().split())
    check.append((c,d))
res_list = []
for i in s:
    a = i[0]
    b = i[1]
    tmp = 1e+9
    res = 0
    for j in range(len(check)):
        c = check[j][0]
        d = check[j][1]
        ans = abs(a-c)+abs(b-d)
        if tmp > ans:
            res = j+1
            tmp = ans
    res_list.append(res)
for i in res_list:
    print(i)
