S = input()

flag = True
for i in range(len(S)):
    if (i+1) % 2 == 0:
        #print(S[i])
        if(S[i] != 'L' and S[i] != 'U' and S[i] != 'D'):
            flag = False
    else:
        if(S[i] != 'R' and S[i] != 'U' and S[i] != 'D'):
            flag = False

if flag:
    print('Yes')
else:
    print('No')
