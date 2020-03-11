def main():
    N = int(input())

    if(N > 1):
        if(N % 2 == 0):
            odd_cnt = N // 2
        if(N % 2 == 1):
            odd_cnt = N // 2 + 1

        print(odd_cnt / N)
    else:
        print(N)


if __name__ == "__main__":
    main()
