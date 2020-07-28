import sys
N = int(input())
S = input()

c = 'b'
cnt = 0

if S == 'b':
    print(0)
    sys.exit()

for i in range(1,N+1):
    cnt+=1
    if i%3==0:
        c ='b'+c+'b'
    elif i%3==1:
        c = 'a'+c+'c'
    elif i%3==2:
        c = 'c'+c+'a'
    if S==c:
        print(cnt)
        break
else:
    print(-1)
