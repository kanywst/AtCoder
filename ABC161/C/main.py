N,K = map(int,input().split())

res = N%K #abs(N-K)
while True:
    tmp = abs(res-K)
    if(res > tmp):
        res = tmp
    else:
        break
print(res)
