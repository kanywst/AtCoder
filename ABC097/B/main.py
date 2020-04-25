import math
X = int(input())

ans = 1
for i in range(int(math.sqrt(X))+1):
    for j in range(int(math.sqrt(X))+1):
        if i**j <= X and ans < i**j:
            ans = i**j
print(ans)
