import sys
input = sys.stdin.readline

N = int(input().rstrip())

Li = [list(map(int, input().split())) for i in range(N)]
Li.sort() # 1번째 전봇대 정렬 , 2번째 전봇대의 부분 수열길이만 고려하면 쉽게 풀림, 1번째는 오름 차순으로 2번째 전봇대 값의 수열로 최대 연결 횟수 구하기 가능

DP = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if Li[i][1] > Li[j][1]: # i 번째의 2번째 전봇대에서 수열이 되면
            DP[i] = max(DP[i], DP[j] + 1) # 이전의 최대 DP or j의 경우 DP

print(N - max(DP)) # 일대일 대응일때 연결 가능한 줄수 N - DP 최대값 = 최소 제거 전기줄 
