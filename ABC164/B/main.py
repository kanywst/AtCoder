A,B,C,D = map(int,input().split())

# A,C 体力
# B,D 攻撃

while True:
    C -= B
    if C <= 0:
        print('YES')
        break
    A -= D
    if A <= 0:
        print('NO')
        break
