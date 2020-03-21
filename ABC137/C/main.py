d,a = {},0
for i in range(int(input())):
    k = ''.join(sorted(input()))
    d[k] = d.get(k,-1)+1
    a+= d[k]
print(a)

'''
N = int(input())
s = list(input() for _ in range(N))

l = sorted(list(map(sorted,s)))
cnt = 0

print(l)
'''
