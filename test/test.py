import sys
input = sys.stdin.readline
N = int(input().rstrip())

for i in range(2, N+1):
    a = 0
    if a == 0:
        while N % i == 0:
            print(i)
            N //= i
    if N - i == 0:
        break
