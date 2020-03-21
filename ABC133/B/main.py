import itertools

N,D = map(int,input().split())

X = [list(map(int,input().split())) for _ in range(N)]

res = list(itertools.combinations(X,2))

cnt = 0

for i in itertools.combinations(X,2):
    tmp = 0
    for j in zip(i[0],i[1]):
        tmp += pow(j[0]-j[1],2)
    ans = tmp ** 0.5
    if ans.is_integer():
        cnt += 1

print(cnt)
