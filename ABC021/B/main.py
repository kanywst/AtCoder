N = int(input())
a,b = map(int,input().split())
K = int(input())
P = list(map(int,input().split())) + [a] + [b]
if len(set(P)) == len(P):
    print('YES')
else:
    print('NO')
