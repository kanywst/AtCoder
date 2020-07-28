from collections import Counter
l = Counter(map(int,input().split()))
for key,value in l.items():
    if value == 1 or value == 3:
        print(key)
