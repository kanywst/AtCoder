import itertools
import math

def solve(l):
    r = 0
    for i in range(len(l)-1):
        x_i = l[i][0]
        y_i = l[i][1]
        x_i_1 = l[i+1][0]
        y_i_1 = l[i+1][1]

        r += math.sqrt(pow(x_i_1 - x_i,2) + pow(y_i_1 - y_i,2))

    return r

def main():
    N = int(input())
    xy = [list(map(int,input().split())) for _ in range(N)]

    p = list(itertools.permutations(xy, len(xy)))
    result = 0

    for i in range(len(p)):
        result += solve(list(p[i]))

    print(result/len(p))



if __name__ == "__main__":
    main()
