S = list(input())

flag = True

if S[0] != 'A':
    flag = False
tmp = S[2:len(S)-1]
if not('C' in tmp and tmp.count('C') == 1):
    flag = False
for i in S:
    if not(i == 'A' or i == 'C') and i.isupper():
        flag = False
        break
print("AC" if flag else "WA")
