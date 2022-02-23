import sys
input = sys.stdin.readline

N = int(input()) # 메모제이션 list bottom-up
dp = [0] * 1000001
dp[1], dp[2] = 1, 2
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[N])

# N = int(input().rstrip()) # 메모제이션 dict top-down # 런타임 에러 (RecursionError) 발생 : Python이 정한 최대 재귀 깊이보다 커서
# sys.setrecursionlimit(10**6) # 최대 재귀 깊이 해결 방법 이지만 실행 값이 커서 안됨
# memo = {1: 1, 2: 2}
# def DP(N):
#     if N in memo:
#         return memo[N]
#     else:
#         memo[N] = (DP(N-1) + DP(N-2))%15746
#         return memo[N]
#
# print(DP(N))
