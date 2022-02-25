import sys
input = sys.stdin.readline

N = int(input())
Li = [list(map(int, input().split())) for i in range(N)]

for i in range(1, len(Li)): # 0,1,2  R G B 각각의 시작 포인트
    Li[i][0] = min(Li[i - 1][1], Li[i - 1][2]) + Li[i][0]
    Li[i][1] = min(Li[i - 1][0], Li[i - 1][2]) + Li[i][1]
    Li[i][2] = min(Li[i - 1][0], Li[i - 1][1]) + Li[i][2]
print(min(Li[N - 1][0], Li[N - 1][1], Li[N - 1][2]))
