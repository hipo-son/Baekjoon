import sys
input = sys.stdin.readline

N = int(input())
Li = [list(map(int, input().split())) for i in range(N)]

for i in range(1, N):
    for j in range(len(Li[i])):
        if j == 0:
            Li[i][j] += Li[i-1][j] # 1열의 경우
        elif j == i:
            Li[i][j] += Li[i-1][j-1] # 사선으 경우
        else:
            Li[i][j] += max(Li[i-1][j], Li[i-1][j-1]) # 나머지 부분의 경우

print(max(Li[N-1]))
