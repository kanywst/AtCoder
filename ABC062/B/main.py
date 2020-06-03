H,W = map(int,input().split())
d = ['#'*(W+2)]
for _ in range(H):
    a = input()
    d.append('#'+a+'#')
d.append('#'*(W+2))
for i in d:
    print(i)
