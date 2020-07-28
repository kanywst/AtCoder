from collections import deque
N,M,L = map(int,input().split())
A = deque(map(int,input().split()))
B = deque(map(int,input().split()))
cnt = 0
while True:
    if L < 0:
        cnt -= 1
        break
    else:
        if len(A) != 0 and len(B) != 0:
            if A[0] < B[0]:
                tmp = A.popleft()
            else:
                tmp = B.popleft()
        elif len(A) != 0 and len(B) == 0:
            tmp = A.popleft()
        elif len(A) == 0 and len(B) != 0:
            tmp = B.popleft()
        else:
            break
        L -= tmp
        cnt += 1

print(cnt)
