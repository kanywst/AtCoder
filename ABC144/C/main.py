import math

def main():
    N = int(input())

    minimum = 10**12
    for i in range(1,math.floor(N**0.5) + 1):
        if(N % i == 0):
            x = i
            y = N // i

            if(minimum > x+y):
                minimum = x + y

    print(minimum - 2)


if __name__ == "__main__":
    main()
