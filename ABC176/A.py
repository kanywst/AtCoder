def main():
    N,X,T = map(int,input().split(' '))
    if N%X==0:
        tmp = N//X
    else:
        tmp = N//X+1
    print(tmp*T)

if __name__ == "__main__":
    main()