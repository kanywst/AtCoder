S = input()

for i in reversed(range(len(S))):
    tmp = S[:i]
    n = len(tmp)//2
    if tmp[:n] == tmp[n:]:
        print(len(tmp))
        break
