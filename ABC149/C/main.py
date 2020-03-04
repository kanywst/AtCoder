def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def main():
    X = int(input())
    for i in range(pow(10,5)):
        num = X + i
        if(is_prime(num)):
            print(num)
            break


if __name__ == "__main__":
    main()
