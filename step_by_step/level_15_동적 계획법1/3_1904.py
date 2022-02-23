import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 1000001
dp[1], dp[2] = 1, 2
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[N])

# N = int(input().rstrip())
# sys.setrecursionlimit(10**6)
# memo = {1: 1, 2: 2}
# def DP(N):
#     if N in memo:
#         return memo[N]
#     else:
#         memo[N] = (DP(N-1) + DP(N-2))%15746
#         return memo[N]
#
# print(DP(N))
