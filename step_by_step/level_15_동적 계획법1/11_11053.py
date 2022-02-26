import sys
input = sys.stdin.readline

N = int(input().rstrip())
Li = list(map(int, input().split()))
DP = [0] * N
for i in range(N):
    for j in range(i):
        if Li[i] > Li[j] and DP[i] < DP[j]: # 현재 i 위치의 Li 값이 이전 원소인 j 보다 크고, 현재 DP 값보다 갱신되는 DP 값이 크다면
            DP[i] = DP[j]
    DP[i] += 1 # 수열인 상황이므로 1을 더한다
print(max(DP))
