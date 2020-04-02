S = list(input())

blue = S.count('1')
red = len(S) - blue

n = min(blue,red)

print(n * 2)
'''
cnt = 0
while True:
    if(S == []):
        break
    for i in range(len(S)-1):
        if(S[i] == '0' and S[i+1] == '1') or (S[i] == '1' and S[i+1] == '0'):
            S = S[:i] + S[i+2:]
            cnt += 2
            break
    else:
        break
print(cnt)
'''
