import sys
input = sys.stdin.readline

N = int(input())
memo = {1: 0, 2: 1}

def DP(N):
    if N in memo:
        return memo[N]

    cnt = 1 + min(DP(N//3) + N % 3, DP(N//2) + N % 2)
    memo[N] = cnt
    return cnt
print(DP(N))
