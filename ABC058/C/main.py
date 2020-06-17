n = int(input())
S = [input() for _ in range(n)]

for i in range(n-1):
    print(set(S[i]) & set(S[i+1]))
