r,D,x = map(int,input().split())

d = [0] * 11
d[0] = x

for i in range(1,11):
    d[i] = r * d[i-1] - D
    print(d[i])
