from collections import Counter
n = int(input())
v = list(map(int,input().split()))
c1 = Counter(v[0::2])
c2 = Counter(v[1::2])

print(c1.most_common())
print(c2.most_common())

'''
n = int(input())
v = list(map(int,input().split()))

cnt = 0
if len(set(v)) < 2:
    cnt += 2
for i in range(n-2):
    if v[i] != v[i+2]:
        cnt+=1
print(cnt)
'''
