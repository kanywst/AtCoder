from collections import Counter
import sys

w = list(input())

for i in Counter(w).values():
    if i%2!=0:
        print('No')
        sys.exit()
print('Yes')
