def main():
    A = list([i for i in input()] for _ in range(10))

    flag = False
    cnt = 0 #もとから島が１つの場合がわからない
    for i in range(len(A[0])):
        for j in range(len(A)):
            if(i - 1 >= 0 and i + 1 < 10 and j - 1 >= 0 and j + 1 < 10):
                if(A[i][j] == 'x'):
                    if(A[i-1][j] == 'o' and A[i+1][j] == 'o'):
                        flag = True
                        cnt += 1
                        #ans = 'YES'
                        #break
                    if(A[i][j-1] == 'o' and A[i][j+1] == 'o'):
                        flag = True
                        cnt += 1
                        #ans = 'YES'
                        #break
        #if(flag):
            #break

    print(cnt)

if __name__ == "__main__":
    main()
