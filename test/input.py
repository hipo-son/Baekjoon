import sys
input = sys.stdin.readline

N = int(input().rstrip())

N, M = map(int, input().rstrip().split())

Li = [int(input().rstrip()) for _ in range(N)]
Li = list(map(int, input().rstrip().split()))


N = int(input().rstrip()) # DP 형식
memo = {}
def DP(N):
    if N in memo:
        return memo[N]
    elif:

print(DP(N)) #
