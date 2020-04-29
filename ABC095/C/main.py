A,B,C,X,Y = map(int,input().split())

tmp = (A+B)//2
ans = 0
if tmp >= C:
    t = min(X,Y)
    X -= t
    Y -= t
    print("t:",t)
    print("X:",X)
    print("Y:",Y)
    ans += t*C*2
    if A<=C*2:
        ans += (X-Y)*A
    else:
        ans += (X-Y)*C*2
    print(ans)
else:
    print(A*X+B*Y)
