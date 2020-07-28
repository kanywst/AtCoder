n = int(input())
a = list(map(int,input().split()))
res = 0
for i in a:
    tmp = i
    while True:
        if tmp%3!=2 and tmp%2!=0:
            res += i-tmp
            break
        else:
            tmp-=1
print(res)
