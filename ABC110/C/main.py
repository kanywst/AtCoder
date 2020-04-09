from collections import Counter
S = sorted(list(input()))
T = sorted(list(input()))

if Counter(Counter(S).values()) == Counter(Counter(T).values()):
    print('Yes')
else:
    print('No')
'''
tmp = copy.copy(S)
for i in tmp:
    if i in T:
        S.remove(i)
        T.remove(i)
if len(set(S)) == len(set(T)):
    print('Yes')
else:
    print('No')
'''
