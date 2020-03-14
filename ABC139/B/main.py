A,B = map(int,input().split())

n = 1
cnt = 0

while n < B:
    n += A-1
    cnt +=1
print(cnt)

'''
result = 0
cnt = 1
for i in range(B):
    if(B - result <= A):
        result +=A
        #cnt += 1
        break
    else:
        cnt += 1
        result += A-1
        print(result)

print(result)
print(cnt)
'''

'''
for i in range(B):
    if A * i >= B:
        print(i)
        break
'''


'''
cnt = B//A
if(B % A == 0):
    print(cnt)
else:
    print(cnt+1)
 '''
