ABC = list(map(int,input().split()))

count = 0
for i in ABC:
    if(i == ABC[0]):
        count += 1
    if(i == ABC[1]):
        count += 1
    if(i == ABC[2]):
        count += 1

count = count - 3
if(count == 2):
    print('Yes')
else:
    print('No')
