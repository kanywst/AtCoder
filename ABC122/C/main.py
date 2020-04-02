N,Q = map(int,input().split())
S = input()
l = [0] * Q
r = [0] * Q

for i in range(Q):
    l[i],r[i] = map(int,input().split())

cs = [0]*(N+1)
for i in range(N-1):
    if(S[i] == 'A' and S[i+1] == 'C'):
        cs[i+2] = cs[i+1] + 1
    else:
        cs[i+2] = cs[i+1]
for q in range(Q):
    print(cs[r[q]] - cs[l[q]])
'''
for i in range(Q):
    l,r = map(int,input().split())
    ques.append((l,r))

for i in ques:
    tmp = S[i[0]-1:i[1]]
    tmp_s = ''.join(tmp)
    print(tmp_s.count('AC'))
'''
