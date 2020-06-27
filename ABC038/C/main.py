N = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in range(N):
    for j in range(N):
        if a[i] > a[j]:
            break
        else:
            print(i+1,j+1)
            cnt+=1
print(cnt)
