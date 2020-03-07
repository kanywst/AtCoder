import math

def main():
    A,B = list(map(int,input().split()))

    ans = -1
    flag = True

    for i in range(1,1010):
        if(math.floor(i*0.08) == A and math.floor(i*0.1) == B):
            ans = i
            flag = False
            break
    print(ans)

if __name__ == "__main__":
    main()
