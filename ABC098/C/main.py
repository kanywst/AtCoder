N = int(input())
S = input()

def f(S):
    cnt = S.count('E')
    for s in S:
        if s == 'E':
            cnt -= 1
        print(cnt)
        yield cnt
        if s == 'W':
            cnt += 1
        #yield cnt

print(list(f(S)))
