import sys
sys.setrecursionlimit(1000000)

def search(x,y):
    if x <0 or y <0 or x>=h or y>=w:
        return
    elif c[x][y] == '#':
        return
    elif c[x][y] == 'g':
        print('Yes')
        exit()
    # c[x][y] = '.'のとき
    c[x][y] = '#'

    search(x-1,y)
    search(x+1,y)
    search(x,y-1)
    search(x,y+1)

    return

h,w = map(int,input().split())
c = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            start_point = (i,j)

# print(start_point)
search(start_point[0],start_point[1])
print('No')
