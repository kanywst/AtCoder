W = input()
res =''
wrong = 'aiueo'
for i in W:
	if i not in wrong:
		res += i
print(res)