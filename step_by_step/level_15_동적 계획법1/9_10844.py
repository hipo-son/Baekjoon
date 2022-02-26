import sys
input = sys.stdin.readline

N = int(input())

DP = [[0] * 10 for i in range(N + 1)]
for i in range(1, 10): # 1일떄의 경우의수
    DP[1][i] = 1
for i in range(2, N + 1):
    for j in range(10): # 2 이상일떄 위치할 수 있는 경우의수
        if j == 0:
            DP[i][j] = DP[i-1][j+1]
        elif j == 9:
            DP[i][j] = DP[i-1][j-1]
        else:
            DP[i][j] = DP[i-1][j+1] + DP[i-1][j-1]

print(sum(DP[N]) % 1000000000)
