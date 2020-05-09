N = int(input())
A = int(input())

tmp = N//500
N -= tmp * 500
if N <= A:
    print('Yes')
else:
    print('No')
