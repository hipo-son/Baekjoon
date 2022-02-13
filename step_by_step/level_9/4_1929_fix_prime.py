import sys
input = sys.stdin.readline
M, N = map(int, input().rstrip().split())

for i in range(M, N+1):
    if i == 1: #1은 소수 X
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)
