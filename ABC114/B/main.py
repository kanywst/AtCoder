S = list(input())

res = 1e+9
for i in range(len(S)-2):
    tmp = S[i:3+i]
    s = abs(int(''.join(tmp)) - 753)
    res = min(s,res)

print(res)
