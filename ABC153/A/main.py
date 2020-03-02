def main():
    H,A = list(map(int,input().split()))
    # H: 体力
    # A: 攻撃
    count = 0
    for _ in range(pow(10,4)):
        H -= A
        count += 1
        if (H <= 0):
            break
    print(count)

if __name__ == "__main__":
    main()
