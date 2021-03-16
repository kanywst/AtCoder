def main():
    N = int(input())
    if sum(list(map(int,list(str(N)))))%9==0:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()