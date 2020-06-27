N,K = map(int,input().split())
D = input().split()

for i in range(N,10*N):
    tmp = list(str(i))
    for j in tmp:
        if j in D:
            break
    else:
        print(''.join(tmp))
        break
