def main():
    A,B,K = list(map(int,input().split()))

    c = K - A
    if(c >= 0):
        result = B-c
        if(result > 0):
            print(0,result)
        else:
            print(0,0)
    else:
        print(A-K,B)


if __name__ == "__main__":
    main()
