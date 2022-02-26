import sys
input = sys.stdin.readline

N = int(input().rstrip())
Li = list(map(int, input().split()))
DP_up, DP_down, DP_total = [0 for i in range(N)], [0 for i in range(N)], [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if Li[i] > Li[j] and DP_up[i] < DP_up[j]:
            DP_up[i] = DP_up[j]
    DP_up[i] += 1

for i in range(N-1, 0-1, -1): # i,j 의 순열만 바꾸면 코딩이 편하다
    for j in range(N-1, i, -1):
        if Li[i] > Li[j] and DP_down[i] < DP_down[j]:
            DP_down[i] = DP_down[j]
    DP_down[i] += 1

for i in range(N):
    DP_total[i] = DP_up[i] + DP_down[i] - 1 # i 에 해당하는 DP 값이 중복되므로 1뺀다

print(max(DP_total))
