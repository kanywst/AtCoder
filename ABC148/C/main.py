import fractions

def lcm(a,b):
    return (a*b) // fractions.gcd(a,b)

def main():
    A,B = list(map(int,input().split()))
    print(lcm(A,B))


if __name__ == "__main__":
    main()
