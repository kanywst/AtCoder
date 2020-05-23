S = input()

for i in range(97,26+97):
    if chr(i) not in S:
        print(chr(i))
        exit(0)
else:
    print('None')
'''
res = ord(S[0])
for i in range(1,len(S)):
    if res+1 == ord(S[i]):
        res = ord(S[i])
    else:
        print(chr(res+1))
        break
else:
    print('None')
'''
