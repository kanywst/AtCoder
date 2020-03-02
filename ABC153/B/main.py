def main():
    H,N = list(map(int,input().split()))
    A = list(map(int,input().split()))

    sum_attack = sum(A)

    if(H <= sum_attack):
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
