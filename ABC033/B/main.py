N = int(input())
s = []
p = []
for _ in range(N):
    S,P = input().split()
    s.append(S)
    p.append(int(P))
for i in range(N):
    if p[i] > sum(p)//2:
        print(s[i])
        break
else:
    print('atcoder')
