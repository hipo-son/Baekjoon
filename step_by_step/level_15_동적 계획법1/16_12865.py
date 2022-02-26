import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

Li = [list(map(int, input().split())) for i in range(N)]
DP = [0] * (K+1) # 무게 0 부터 K 까지

for _ in Li:
    W, V = map(int, _) # Li 의 W, V 값
    for j in range(K, W-1, -1):
        DP[j] = max(DP[j], DP[j-W] + V)

print(DP[-1])
