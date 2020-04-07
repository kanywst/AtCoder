import sys

s = int(input())

res = [s]
c = 0
while True:
    if(res[c]%2 == 0):
        tmp = res[c]//2
    if(res[c]%2 == 1):
        tmp = res[c]*3+1
    res.append(tmp)
    if(len(set(res)) != len(res)):
        print(c+2)
        sys.exit()
    c+=1
