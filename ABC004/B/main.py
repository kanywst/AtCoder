c = []
for _ in range(4):
    c = input().split()[::-1] + c
for i in range(0,len(c),4):
    print(' '.join(c[i:i+4]))
