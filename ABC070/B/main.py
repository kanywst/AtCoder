#l = list(map(int,input().split()))
A,B,C,D = map(int,input().split())

print(max(min(B,D)-max(A,C),0))

'''
if l[1] >= l[2]:
    l.sort()
    print(l[2]-l[1])
else:
    print(0)
'''
