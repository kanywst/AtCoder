def main():
    S = input()
    length = len(S)
    loop_count = length // 2
    count = 0

    for i in range(loop_count):
        if(S[i] != S[length - i -1]):
            #print(S[i],"==",S[loop_count - i -1])
            count += 1

    print(count)


if __name__ == "__main__":
    main()
