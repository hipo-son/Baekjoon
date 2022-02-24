import sys
input = sys.stdin.readline

T = int(input())
memo = [0] * 101
memo[1] = 1
memo[2] = 1
memo[3] = 1
for _ in range(4, 101):
    memo[_] = memo[_-2] + memo[_-3]
for i in range(T):
    p = int(input())
    print(memo[p])
