def main():
    N,K,M = list(map(int,input().split()))
    A = list(map(int,input().split()))

    av = N * M
    ans = av - sum(A)
    if(ans < 0):
        print(0)
    elif(ans > K):
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()
