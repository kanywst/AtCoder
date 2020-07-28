from collections import Counter
S = Counter(list(input()))
res = {'A':0,
       'B':0,
       'C':0,
       'D':0,
       'E':0,
       'F':0}
for i,j in S.items():
    res[i] = j
print(' '.join(map(str,res.values())))
