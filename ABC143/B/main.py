import itertools

def main():
    N = int(input())
    d = list(map(int,input().split()))

    result = 0

    for i in itertools.permutations(d,2):
        result += i[0] * i[1]

    print(result // 2)


if __name__ == "__main__":
    main()
