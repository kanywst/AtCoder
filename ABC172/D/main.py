N = int(input())

def div(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

res = 0

for i in range(1,N+1):
    tmp = len(div(i)[0:])
    res += i*tmp
print(res)
