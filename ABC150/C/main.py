import itertools

def main():
    N = int(input())
    P = list(map(int,input().split()))
    Q = list(map(int,input().split()))

    N_range = [i for i in range(1,N+1)]

    p = list(itertools.permutations(N_range,N))
    #print(list(p[0]))
    #print(P)

    start = 0
    end = 0

    for i in range(len(p)):
        if(list(p[i]) == P):
            start = i
        if(list(p[i]) == Q):
            end = i

    if(start > end):
        print(start - end)
    else:
        print(end - start)

if __name__ == "__main__":
    main()
