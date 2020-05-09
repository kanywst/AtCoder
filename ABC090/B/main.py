A,B = map(int,input().split())

cnt = 0
for i in range(A,B+1):
    n = str(i)
    if n == n[::-1]:
        cnt += 1
print(cnt)
