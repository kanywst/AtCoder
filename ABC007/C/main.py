from collections import deque

R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
c = [list(input()) for _ in range(R)]

def bfs():
    d = [[float("inf")] * C for _ in range(R)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque([])
    #que.append((sx,sy))
    #d[sx][sy] = 0
    que.append((sy,sx))
    d[sy][sx] = 0

    while que:
        p = que.popleft()
        #if p[0] == gx and p[1] == gy:
        if p[0] == gy and p[1] == gx:
            break

        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if 0 <= nx < R and 0 <= ny < C and c[nx][ny] != '#' and d[nx][ny] == float("inf"):
                que.append((nx,ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    return d[gy][gx]

sx -= 1
sy -= 1
gx -= 1
gy -= 1

print(bfs())
