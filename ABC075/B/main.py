'''
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

def check(y, x):
    dx = [1, 0, -1]
    dy = [1, 0, -1]
    for i in dy:
        for j in dx:
            nx = x + j
            ny = y + i
            if 0<=nx<w and 0<=ny<h:
                if  s[ny][nx] == '#':
                    s[y][x] += 1

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            s[i][j] = 0
            check(i, j)

for i in s:
    print(''.join(map(str, i)))
'''
H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]


def check(y,x):
    dx = [1,0,-1]
    dy = [1,0,-1]
    for i in dy:
        for j in dx:
            nx = x + j
            ny = y + i
            if 0<=nx<W and 0<=ny<H:
                if S[ny][nx] == '#':
                    print(S[y][x])
                    S[y][x] += 1

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            S[i][j] = 0
            check(i,j)

for i in S:
    print(''.join(map(str,i)))


'''
d = [['#']*W]*H
cnt = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
#            continue
#            print(i,j)
            d[i][j] = '#'
        else:
            if i-1>=0 and S[i-1][j] == '#':
                cnt += 1
            if i-1>=0 and j-1>=0 and S[i-1][j-1] == '#':
                cnt += 1
            if i-1>=0 and j+1<W and S[i-1][j+1] == '#':
                cnt += 1
            if i-1>=0 and S[i][j-1] == '#':
                cnt += 1
            if j+1<W and S[i][j+1] == '#':
                cnt += 1
            if i+1<H and S[i+1][j] == '#':
                cnt += 1
            if i+1<H and j-1>=0 and S[i+1][j-1] == '#':
                cnt += 1
            if i+1<H and j+1<W and S[i+1][j+1] == '#':
                cnt += 1
            S[i][j] = str(cnt)
        cnt = 0

for i in range(H):
    print(''.join(S[i]))
'''
