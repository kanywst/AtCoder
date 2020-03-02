def main():
    N,M = list(map(int,input().split()))
    sc = [list(map(int,input().split())) for _ in range(M)]

    ans = [0 for _ in range(N)]

    for i in range(M):
        s = sc[i][0]
        c = sc[i][1]

        if(c != 0):
            ans[s-1] = c

    result = "".join(list(map(str,ans)))
    if(len(str(int(result))) == N):
        print(result)
    else:
        print(-1)
#    flag = False
#    count = 0

#    for i in range(N-1):
#        if(ans[i] != 0):
#            if(count > 0):
#                flag = True
#            else:
#                flag = False
#            break
#        elif(ans[i] == 0):
#            flag = True
#            count += 1

#    if(flag):
#        print(-1)
#    else:
#        print("".join(list(map(str,ans))))

if __name__ == "__main__":
    main()
