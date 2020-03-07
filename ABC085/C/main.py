def main():
    N,Y = list(map(int,input().split()))

    flag = False

    loop_10000 = Y // 10000
    loop_5000 = Y // 5000
    loop_1000 = Y // 1000

    for i in range(loop_10000+1):
        for j in range(loop_5000+1):
            k = N - i - j
            if(k >= 0 and i+j+k == N and 10000 * i + 5000 * j + 1000 * k == Y):
                print(i,j,k)
                flag = True
                break
            #for k in range(loop_1000+1):
            #    if(i+j+k == N and 10000 * i + 5000 * j + 1000 * k == Y):
            #        print(i,j,k)
            #        flag = True
            #        break
            #if(flag):
            #    break
        if(flag):
            break
    if(not flag):
        print(-1,-1,-1)

if __name__ == "__main__":
    main()
