D,G = map(int,input().split())
cnt = 1e+9
for i in range(D):
    p,c = map(int,input().split())
    point = (i+1)*100
    tmp = G // point
    #print("tmp:",tmp)
    if tmp < p:
        cnt = min(tmp+1,cnt)
    else:
        print("i:",i)
        if tmp*point+c >= G:
            #print("tmp:",p)
            cnt = min(p,cnt)
print(cnt)
