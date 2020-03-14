N = int(input())
v = list(map(int,input().split()))

v_r = sorted(v)
result = 0
tmp = (v_r[0] + v_r[1]) / 2
for i in range(2,N):
    #print(temp)
    tmp = (tmp + v_r[i]) / 2
print(tmp)
