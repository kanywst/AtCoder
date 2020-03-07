def main():
    S = list(map(int,list(input())))

    result = 0
    symbols = list()
    answer = ''

    for j in range(pow(2,len(S)-1)):
        for i in range(len(S)):
            print(j,i)
            if(j % 2 == 0):
                result += S[i]
                symbols.append('+')
            if(j % 2 == 1):
                result -= S[i]
                symbols.append('-')

        if(result == 7):
            print(symbols)
            break
        else:
            symbols.clear()
            result = 0

    answer += str(S[0])
    answer += symbols[0]
    answer += str(S[1])
    answer += symbols[1]
    answer += str(S[2])
    answer += symbols[2]
    answer += str(S[3])
    answer += '=7'

    print(answer)
    #print(S)

if __name__ == "__main__":
    main()
