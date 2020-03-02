N = int(input())
X = list(map(int, input().split()))

min = 1000000
result = 0
for i in range(100):
    for j in X:
        result += (i + 1 - j) ** 2
    if min > result:
        min = result
    result = 0

print(min)
