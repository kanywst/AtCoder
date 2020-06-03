N = int(input())
a = [int(input()) for _ in range(N)]

i = 0
cnt = 1
while True:
    if cnt > len(a):
        cnt = -1
        break
    if a[i] == 1:
        cnt = -1
        break
    elif a[i] == 2:
        break
    else:
        i = a[i] - 1
        cnt += 1
print(cnt)
