def main():
    N = int(input())
    S = input()

    ans = ''
    for i in range(len(S)):
        o = (ord(S[i]) - 65 + N)%26 + 65
        ans += chr(o)
    print(ans)

if __name__ == "__main__":
    main()
