N = int(input())
W = list(map(int,input().split()))

res = 10**10

for i in range(1,N):
    tmp1 = W[:i]# + W[i:]
    tmp2 = W[i:]

    sum_tmp1 = sum(tmp1)
    sum_tmp2 = sum(tmp2)

    ans = abs(sum_tmp1 - sum_tmp2)

    if(ans < res):
        res = ans
print(res)
