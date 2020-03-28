import itertools

N,M = map(int,input().split())


n = list(itertools.combinations(list(range(N)),2));
m = list(itertools.combinations(list(range(M)),2));

print(len(n) + len(m))
