def main():
    n = [int(x) for x in input()]
    op_cnt = len(n) - 1
    for i in range(2 ** op_cnt):
        op = ["-"] * op_cnt
        for j in range(op_cnt):
            if ((i >> j) & 1):
                op[op_cnt - 1 -j] = "+"
        #print(op)
        formula = ""
        #print(list(zip(n,op + [""])))
        for p_n,p_o in zip(n,op + [""]):
            formula += (str(p_n) + p_o)
        #print(formula)
        if eval(formula) == 7:
            print(formula + "=7")
            break


if __name__ == "__main__":
    main()
