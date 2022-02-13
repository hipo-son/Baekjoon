import sys
input = sys.stdin.readline
T = int(input().rstrip())

for i in range(T):
    n = int(input().rstrip())
    for i in range(1, n+1):
        if i == 1: #1은 소수 X
            continue
        for j in range(2, int(i ** 0.5)+1 ):
            if i%j==0:
                break
        else:
            last_i = i
    print(last_i)
