import sys
N = int(input())
ans = 0
def dfs(n):
    if n == N:
        print('Yes')
        sys.exit()
    if n > N:
        return

    dfs(n+4)
    dfs(n+7)

dfs(0)
print('No')
