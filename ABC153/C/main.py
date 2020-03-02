def main():
    N,K = list(map(int,input().split()))
    H = list(map(int,input().split()))

    sorted_H = sorted(H,reverse=True)

    for i in range(K):
        if(i < len(sorted_H)):
            sorted_H[i] = 0

    '''
    for _ in range(K):
        if(len(H) > 0):
            maximum = max(H)
            H.remove(maximum)
            '''

    print(sum(sorted_H))

if __name__ == "__main__":
    main()
