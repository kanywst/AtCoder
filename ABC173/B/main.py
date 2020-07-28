from collections import Counter
N = int(input())
d = {'AC':0,
     'WA':0,
     'TLE':0,
     'RE':0}
for key,value in Counter([input() for _ in range(N)]).items():
    d[key]=value

for key,value in d.items():
    print(key,'x',value)
