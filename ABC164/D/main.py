S = input()

cnt = 0
d = []
for i in range(1,100000):
    tmp = str(i*2019)
    cnt += S.count(tmp)
    cnt += S.count(tmp+tmp[1:])
print(cnt)

'''
for i in range(4,len(S)):
    for j in range(len(S)):
        if j+i <= len(S):
            tmp = S[j:j+i]
            if int(tmp) % 2019 == 0:
                cnt += 1
print(cnt)
'''
