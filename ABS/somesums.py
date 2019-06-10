# n,a,b = map(int,[input() for i in range(0,3)])
n,a,b = map(int,input().split())
result = 0
for i in range(1,n+1):
    if a <= sum(map(int,list(str(i)))) <= b:
        result += i
print(result)
