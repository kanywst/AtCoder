def main():
    A,B = map(int,input().split())
    max_follow = 2 * A + 100
    print(max_follow-B)

if __name__ == "__main__":
    main()