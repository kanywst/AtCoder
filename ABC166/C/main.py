N,M = map(int,input().split())
H = list(map(int,input().split()))

d = []
for i in range(M):
    A,B = map(int,input().split())
    d.append((A-1,B-1))

flag = {}
for i in range(N):
    flag[i] = True

for i in d:
    A = i[0]
    B = i[1]
    if not(H[A] > H[B] and flag[A] == True):
        flag[A] = False
    if not(H[B] > H[A] and flag[B] == True):
        flag[B] = False
print(list(flag.values()).count(True))
