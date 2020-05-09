import sys
A,B = map(int,input().split())
S = input()

flag = True
if not(len(S) == A+B+1):
    flag = False
if not(S[A] == '-'):
    flag = False
for i in range(A+B+1):
    if i != A:
        if not(48<=ord(S[i])<=57):
            flag = False
if flag:
    print('Yes')
else:
    print('No')
