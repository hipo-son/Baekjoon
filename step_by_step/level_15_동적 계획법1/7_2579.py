import sys
input = sys.stdin.readline

N = int(input())
Li = [0] + [int(input()) for i in range(N)]
DP = [0] * (N+1) # 총합

DP[1] = Li[1] # 계단 한칸일때
if N >= 2: # 두칸 이상일때
    DP[2] = max(Li[1]+Li[2], Li[2])
for i in range(3, N+1):
    DP[i] = max(Li[i] + Li[i-1] + DP[i-3], Li[i] + DP[i-2])
print(DP[N])
