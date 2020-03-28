def euclid(a, b):
    while b:
        a, b = b, a%b
    return a

def multiple(a, b):
    return a*b // euclid(a, b)

A,B,C,D = map(int,input().split())

all = B - A + 1
x = B//C - (A-1)//C
y = B//D - (A-1)//D
lcm = multiple(C,D)
z = B//lcm - (A-1)//lcm

print(all - x - y + z)
'''
cnt = 0
for i in range(A,B+1):
    if(i%C != 0 and i%D != 0):
        cnt += 1
print(cnt)
'''
