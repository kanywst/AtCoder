from itertools import combinations
import sys

x = [input() for _ in range(5)]
k = int(input())

for i in combinations(x,2):
    tmp = abs(int(i[0])-int(i[1]))
    if(tmp > k):
        print(':(')
        sys.exit()
print('Yay!')
