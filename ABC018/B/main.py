S = input()
N = int(input())
for _ in range(N):
    l,r = map(int,input().split())
    tmp = S[l-1:r]
    S = S[:l-1] + tmp[::-1] + S[r:]
print(S)
