S = list(input())
K = int(input())

cnt = 0
tmp = 0
for i in range(K):
    if S[i] == '1':
        cnt += 1
    else:
        tmp = S[i]
        break
if K <= cnt:
    print(1)
else:
    print(tmp)
