def main():
    A = [list(map(int,input().split(" "))) for i in range(3)]
    N = int(input())
    b_list = [int(input()) for _ in range(N)]

    for i in range(3):
        for j in range(3):
            for b in b_list:
                if(A[i][j] == b):
                    A[i][j] = 0

    flag = False
    for i in range(3):
        for j in range(3):
                if(j+2 < 3 and A[i][j] == 0 and A[i][j+1] == 0 and A[i][j+2] == 0):
                    flag = True
                    break
                if(i+2 < 3 and A[i][j] == 0 and A[i+1][j] == 0 and A[i+2][j] == 0):
                    flag = True
                    break
                if(i+2 < 3 and j+2 < 3 and A[i][j] == 0 and A[i+1][j+1] == 0 and A[i+2][j+2] == 0):
                    flag = True
                    break
                if(i-2 >= 0 and j-2 >= 0 and A[i][j] == 0 and A[i-1][j-1] == 0 and A[i-2][j-2] == 0):
                    flag = True
                    break
                if(i-2 >= 0 and j+2 < 3 and A[i][j] == 0 and A[i-1][j+1] == 0 and A[i-2][j+2] == 0):
                    flag = True
                    break
                if(i+2 < 3 and j-2 >= 0 and A[i][j] == 0 and A[i+1][j-1] == 0 and A[i+2][j-2] == 0):
                    flag = True
                    break
        if(flag):
            break

    if(flag):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
