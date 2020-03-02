import sys

def main():
    input = sys.stdin.readline

    N = int(input())
    P = list(map(int,input().split()))

    #result = list()

    minimum = P[0]
    count = 1
    for i in range(N):
        if(minimum > P[i]):
            minimum = P[i]
            count += 1
    print(count)
#        Pj = list(P[j] for j in range(i+1))
        #print(Pj)
        #Pj = P[0:i+1]
#        min_P = min(Pj)
#        result.append(min_P)
#        print(min_P)
#        if(P[i] == min_P):
#            count += 1

    '''
    count = 0
    flag = True

    for i in range(N):
        for j in range(i):
            if(P[i] > P[j]):
                flag = False
                break
        if(flag):
            count += 1
        flag = True
    print(count)
    '''

if __name__ == "__main__":
    main()
