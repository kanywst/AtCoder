def main():
    N = int(input())
    S = list(input())

    flag = False

    for i in range(N):
        T1 = S[:i]
        T2 = S[i:N]

        if(T1 == T2):
            flag = True
            #print('Yes')
            break

        # print(T1)
        # print(T2)
    if(flag):
        print('Yes')
    else:
        print('No')
if __name__ == "__main__":
    main()
