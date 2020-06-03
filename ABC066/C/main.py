from collections import deque

n = int(input())
a = list(map(int,input().split()))

d = deque()

for i in range(n):
    if n%2 == 0 and i%2 == 0:
        #d.append(a[i])
        d.append(a[i])
    elif n%2==1 and i%2==1:
        d.append(a[i])
    else:
        d.appendleft(a[i])
        #d.appendleft(a[i])
print(' '.join(map(str,list(d))))
