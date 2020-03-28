S = list(input())
N = len(S)
n1 = (N - 1) // 2
n2 = (N + 3) // 2

res1 = S[:n1]
res2 = S[n2-1:]

if(S == list(reversed(S)) and res1 == list(reversed(res1)) and res2 == list(reversed(res2))):
    print('Yes')
else:
    print('No')
