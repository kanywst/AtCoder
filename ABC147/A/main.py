def main():
    A1,A2,A3 = list(map(int,input().split()))

    if(A1+A2+A3 < 22):
        print('win')
    else:
        print('bust')

if __name__ == "__main__":
    main()
