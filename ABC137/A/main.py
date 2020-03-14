A,B = map(int,input().split())

plus = A + B
minus = A - B
div = A * B

tmp = max(plus,minus)
result = max(div,tmp)

print(result)
