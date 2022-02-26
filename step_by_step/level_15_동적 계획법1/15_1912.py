import sys
input = sys.stdin.readline

N = int(input())
Li = list(map(int, input().split()))
DP = [0] * N
DP[0] = Li[0] # N이 1일때는 DP 값이 Li[0] 과 동일
for i in range(1, N):
    DP[i] = max(Li[i], DP[i-1] + Li[i]) # i 번째 수가 연속적인 수열이 아닐떄, 수열일때 중 큰값을 DP 로 저장

print(max(DP))
