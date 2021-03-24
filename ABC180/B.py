def main():
    N = int(input())
    x = list(map(abs,(map(int,input().split(' ')))))
    a = sum(x)
    c = max(x)
    y = list(map(lambda x: x**2,x))
    b = sum(y)**0.5
    print(a)
    print(b)
    print(c)


if __name__ == "__main__":
    main()