A,B,C,K = map(int,input().split())

if K <= A:
    value = K
else:
    value = A + B*0
cnt = A + B
#value = A + B*0
if cnt >= K:
    print(value)
else:
    value -= K - cnt
    print(value)
