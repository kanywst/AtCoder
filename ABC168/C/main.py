import math
A,B,H,M = map(int,input().split())

tmp = M * 0.5
if H == 0:
    H = 12
if M == 0:
    M = 60

h = H*30
m = (M/5)*30

if h >= m:
    rad = (h+tmp)-(m)
else:
    rad = (m)-(h+tmp)

ans = A**2 + B**2 - 2*A*B*(math.cos(math.radians(rad)))
print(ans**0.5)
