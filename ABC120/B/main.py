A,B,K = map(int,input().split())

x = 0
m = 1

x = 0
for i in range(100,0,-1):
  if (A%i == 0) and (B%i == 0):
    x += 1
    if x == K:
      print(i)
      break
    
'''
while m:
    if(A%m == 0 and B%m == 0):
        x+=1
        if(x == K):
            print(m)
            break
    m+=1
'''
'''
m = 1
res = 0
cnt = 0
while m:
    if(K == cnt):
        break
    if(A%m == 0 and B%m == 0):
        cnt += 1
        res = m
        print(m)
    m+=1
print(res)
'''
