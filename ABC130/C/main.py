W,H,x,y = map(int,input().split())

s = (W*H)/2
c = 0

if(W == x*2 and H == y*2):
    c = 1
print(s,c)
