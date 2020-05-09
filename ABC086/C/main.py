import sys
N = int(input())
l = [list(map(int,input().split())) for _ in range(N)]

sys.setrecursionlimit(10 ** 6)

def f(x,y,t,gx,gy,gt):
    if x<0 or y<0:
        return False
    if t >= gt:
        if x == gx and y == gy:
            return x,y,t
        else:
            return False
    #print('1')
    f(x+1,y,t+1,gx,gy,gt)
    #print('2')
    f(x-1,y,t+1,gx,gy,gt)
    #print('3')
    f(x,y+1,t+1,gx,gy,gt)
    #print('4')
    f(x,y-1,t+1,gx,gy,gt)

x,y,t = 0,0,0
for i in l:
    gt,gx,gy = i[0],i[1],i[2]
    print(f(x,y,t,gx,gy,gt))
