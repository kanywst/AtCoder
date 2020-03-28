N = int(input())
'''
SP = [list(input().split()) for _ in range(N)]

tmp = sorted(SP)

print(tmp)
'''

d = []
for i in range(N):
    S,P = input().split()
    d.append([S,int(P),i])

d.sort(key=lambda x:(x[0],-x[1]))

for i in d:
    print(i[2]+1)
