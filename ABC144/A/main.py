def main():
    A,B = list(map(int,input().split()))

    if(A <= 9 and B <= 9):
        print(A*B)
    else:
        print(-1)

if __name__ == "__main__":
    main()
