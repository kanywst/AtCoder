def main():
    N = int(input())
    cnt = 0
    ok = False
    for i in range(N):
        d1,d2 = map(int,input().split(' '))
        if d1 == d2:
            cnt+=1
        else:
            cnt = 0
        if cnt == 3:
            ok = True
    print('Yes' if ok else 'No')

if __name__ == "__main__":
    main()