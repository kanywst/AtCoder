N = int(input())

print(sum(len(str(i)) % 2 for i in range(1,N+1)))

'''
result = 0
if(0<N<=pow(10,5)):
    if len(str(N)) % 2 == 0:
        loop = ((len(str(N)) - 1) -1) //2 + 1
        for i in range(loop):
            result += 9 * pow(10,2*i)
    else:
        for i in range(len(str(N)) - 2):
            result += 9 * pow(10,i)
        result += N - pow(10,len(str(N)) - 1) + 1

print(result)
'''
