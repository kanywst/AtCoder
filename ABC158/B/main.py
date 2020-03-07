def main():
    N,A,B = list(map(int,input().split()))

    b = 'b'*A
    r = 'r'*B
    br = b + r

    if(N > 0 and A >= 0 and B >= 0):
        result = br * N

        if(len(result) > N):
            print(result[:N].count('b'))
        else:
            print(result.count('b'))
    else:
        print(0)

if __name__ == "__main__":
    main()
