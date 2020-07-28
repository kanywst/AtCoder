N = int(input())
if N%1000==0:
    print(0)
else:
    tmp = N//1000
    res = tmp+1
    print(res*1000-N)
