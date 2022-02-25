import sys
input = sys.stdin.readline

N = int(input())
Li = [list(map(int, input().split())) for i in range(N)]

for i in range(1, N):
    for j in range(len(Li[i])):
        if j == 0:
            Li[i][j] += Li[i-1][j]
        elif j == i:
            Li[i][j] += Li[i-1][j-1]
        else:
            Li[i][j] += max(Li[i-1][j], Li[i-1][j-1])

print(max(Li[N-1]))
