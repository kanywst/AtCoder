n,m = map(int,input().split())

a = ((n%12)*60+m)/2
b = 6*m
c = abs(a-b)%360
print(min(c,360-c))
