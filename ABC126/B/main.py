S = list(input())

d = []
d.append(int(S[0]+S[1]))
d.append(int(S[2]+S[3]))

res = []
if(1<= d[0] <= 12):
    res.append('MMYY')
    # MMYY
if(1<= d[1] <= 12):
    res.append('YYMM')
    # YYMM
if(res == []):
    print('NA')
elif(len(res) == 1 and res[0] == 'MMYY'):
    print('MMYY')
elif(len(res) == 1 and res[0] == 'YYMM'):
    print('YYMM')
else:
    print('AMBIGUOUS')
#print(res)
