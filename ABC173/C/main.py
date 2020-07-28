import copy
import sys
H,W,K = map(int,input().split())
c = [list(input()) for _ in range(H)]

def solve(ret):
    res = 0
    for i in range(W):
        for j in range(H):
            l = copy.copy(ret)
            for x in range(j):
                l = l[:x] + l[x+1:]
            for y in range(i):
                l = l[x][:y] + l[x][y+1:]
            ans = 0
            for k in l:
                ans += k.count('#')
                if ans == K:
                    res += 1
    return res
print(solve(c))
