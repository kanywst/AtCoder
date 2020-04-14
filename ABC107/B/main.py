H,W = map(int,input().split())
a = ['']*H
for i in range(H):
    a[i] = input()

row = [False] * H
col = [False] * W

for i in range(H):
    for j in range(W):
        if a[i][j] == '#':
            row[i] = True
            col[j] = True
print("row:",row)
print("col:",col)
