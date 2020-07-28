S = input()
cnt = 0
for i in S.split('+'):
    if not('0' in i):#eval(i) != 0:
        cnt+=1
print(cnt)
