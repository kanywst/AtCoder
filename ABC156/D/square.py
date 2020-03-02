def pow(x,n):
    ans = 1
    while(n > 0):
        if(bin(n & 1) == bin(1)):
            ans = ans * x
        x = x * x
        n = n >> 1
    return ans

result = pow(2,1000000000)
print(result)
