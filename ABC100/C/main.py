N = int(input())
a = list(map(int,input().split()))

l = []
for i in a:
    if i % 2 == 0:
        l.append(i)
l.sort()
c = 0
while True:
    if len(l) == 0:
        break
    if len(l) == 1 and l[0] % 2 == 1:
        break
    if l[0] == 1:
        l = l[1:]
    else:
        l[0] = l[0] // 2
        l[1:] = list(map(lambda x:x*3,l[1:]))
        c += 1
    print(l)
    print(c)
print(c)
