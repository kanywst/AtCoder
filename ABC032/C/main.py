N,K = map(int,input().split())
s = [int(input()) for _ in range(N)]

def f(lst):
    for i in range(1,len(lst)):
        lst[i] *= lst[i-1]
    return lst

print(f(s))
