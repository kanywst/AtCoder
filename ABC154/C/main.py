def main():
    N = int(input())
    A = list(map(int,input().split()))

    set_A = set(A)

    if(len(set_A) == len(A)):
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
