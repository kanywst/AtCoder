def main():
    N = int(input())
    S = [input() for _ in range(N)]#list()

    target = {}

    for word in S:
        if word in target:
            target[word] += 1
        else:
            target[word] = 1

    maximum = max(target.values())

    for key,val in sorted(target.items()):
        if(val == maximum):
            print(key)

if __name__ == '__main__':
    main()
