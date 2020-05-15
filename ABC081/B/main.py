N = int(input())
A = list(map(int,input().split()))

cnt = 0
flag = False
while True:
    for i in range(N):
        if A[i] % 2 == 1:
            flag = True
            break
    else:
        cnt += 1
    if flag:
        break
    A = list(map(lambda x:x//2,A))
print(cnt)
