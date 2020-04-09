n = list(input())

res = []
for i in n:
    if i == '1':
        res.append('9')
    elif i == '9':
        res.append('1')
    else:
        res.append(i)
print(''.join(res))    
