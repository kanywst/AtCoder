import copy
import sys

A = [list(input()) for _ in range(10)]

def dfs(x,y):
    if(not(0<=x<10) or not(0<=y<10) or A_copy[x][y] == 'x'):
        return
    if(A_copy[x][y] == 'o'):
        A_copy[x][y] = 'x'

    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)

for i in range(10):
    for j in range(10):
        A_copy = copy.deepcopy(A)
        if(A_copy[i][j] == 'x'):
            A_copy[i][j] = 'o'

        dfs(i,j)

        flag = True
        for k in range(10):
            for l in range(10):
                if(A_copy[k][l] != 'x'):
                    flag = False
                    break
        if flag:
            print('YES')
            sys.exit()


        #print(A_copy)
print('NO')
