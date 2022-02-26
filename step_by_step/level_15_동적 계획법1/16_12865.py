import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

Li = [list(map(int, input().split())) for i in range(N)]
DP = [0] * (K+1) # 무게 0 부터 K 까지

for _ in Li:
    W, V = map(int, _) # Li 의 W, V 값
    for j in range(K, W-1, -1):
        DP[j] = max(DP[j], DP[j-W] + V) # 현재 DP 의 값 or 해당 W 와 V 조건일때 더 큰값 선택 

print(DP[-1])
