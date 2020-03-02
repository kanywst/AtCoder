def main():
    N = int(input())
    cal = N>>1
    if(N%2 == 0):
        print(cal)
    else:
        print(cal+1)

if __name__ == "__main__":
    main()
