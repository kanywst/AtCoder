N,K = map(int,input().split())
S = list(input())


for i in range(N):
    if(i+1 == K):
        S[i] = chr(ord(S[i]) + 32)
print(''.join(S))
