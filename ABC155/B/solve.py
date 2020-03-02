N = int(input())
A_i = list(map(int,input().split()))

flag = 0
even = list()

for i in range(N):
    if (A_i[i] % 2 == 0):
        even.append(A_i[i])

for i in even:
    if (i % 3 == 0 or i % 5 == 0):
        flag += 1

if(flag == len(even)):
    print('APPROVED')
else:
    print('DENIED')
