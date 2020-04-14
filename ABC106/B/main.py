N = int(input())

d = []
cnt = 0
for i in range(1,N+1):
    if i % 2 == 1:
        for j in range(1,int(i**0.5)+1):
            if i % j == 0:
                d.append(j)
                if j != i//j:
                    d.append(i//j)
        if len(d) == 8:
            cnt +=1
        d = []
print(cnt)
