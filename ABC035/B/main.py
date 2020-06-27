from collections import Counter
S = list(input())
T = int(input())
x,y = 0,0
cnt = Counter(S)
x -= cnt['L']
x += cnt['R']
y += cnt['U']
y -= cnt['D']
if T == 1:
    print(abs(x)+abs(y)+cnt['?'])
else:
    print(abs(abs(x)+abs(y)-cnt['?']))
