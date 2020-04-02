X = int(input())

res = 0

tmp = X//500
res += tmp * 1000
X -= tmp * 500

tmp = X//5
res += tmp * 5

print(res)
