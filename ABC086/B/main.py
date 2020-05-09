a,b= input().split()

n = int(a+b)
if any(i**2 == n for i in range(n//2)):
    print('Yes')
else:
    print('No')
