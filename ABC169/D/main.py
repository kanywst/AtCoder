N = int(input())

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

cnt = 0
while True:
    if is_prime(N) or N ==1:
        print(cnt)
        break
    else:
        tmp = make_divisors(N)[1:]
        for i in tmp:
            if N % i == 0:
                N = N//i
                cnt += 1
                break
