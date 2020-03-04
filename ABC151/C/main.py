def main():
    N,M = list(map(int,input().split()))
    pS = [input().split() for _ in range(M)]

    problem_number = 1

    ac = 0
    ac_count = 0
    wa_count = 0
    wa = 0

    for i in range(M):
        if(problem_number == int(pS[i][0])):
            if(pS[i][1] == 'WA'):
                wa_count += 1
            if(pS[i][1] == 'AC'):
                if(ac_count == 0):
                    print(ac_count)
                    ac += 1
                    ac_count += 1
                    wa += wa_count
                    wa_count = 0

        else:
            wa_count = 0
            problem_number += 1
            if(pS[i][1] == 'WA'):
                wa_count += 1
            if(pS[i][1] == 'AC'):
                if(ac_count == 0):
                    ac_count += 1
                    ac+=1

    print(ac,wa)


if __name__ == "__main__":
    main()
