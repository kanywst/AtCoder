s = input()

n = 0
m = 0
for i in range(len(s)):
    if s[i] == 'A':
        n = i
        break
for i in reversed(range(len(s))):
    if s[i] == 'Z':
        m = i
        break
print(m-n+1)
