def main():
    S,T = list(input().split())
    A,B = list(map(int,input().split()))
    U = input()

    if(S == U):
        result = [A - 1,B]

    if(T == U):
        result = [A,B - 1]

    print(" ".join(list(map(str,result))))

if __name__ == "__main__":
    main()
