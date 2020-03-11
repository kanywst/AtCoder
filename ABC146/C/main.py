import math

def main():
    A,B,X = list(map(int,input().split()))

    result = 0

    for i in range(1,19):
        ans = X - i*B
        if(ans > 0):
            result = math.floor(ans / A)
            print(result)

    print(result)

if __name__ == "__main__":
    main()
