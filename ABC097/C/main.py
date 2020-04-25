from itertools import combinations

s = input()
K = int(input())


for i in range(len(s)):
    for j in range(len(s)):
        print("i:j",j,",",i)
        print(s[i:] + s[:j])
