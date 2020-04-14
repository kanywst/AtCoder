import copy

tmp = list(range(1,int(input())+1))

#tmp = copy.copy(N)
res = 0
for i in range(len(tmp)):
    if tmp[i] % 3 != 0 and tmp[i] % 5 != 0 and tmp[i] % 15 != 0:
        res += tmp[i]

print(res)
