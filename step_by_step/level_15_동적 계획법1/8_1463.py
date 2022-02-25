import sys
input = sys.stdin.readline

N = int(input())
memo = {1: 0, 2: 1}

def DP(N):
    if N in memo:
        return memo[N]
# 1 : 마지막 3또는 2의 경우 한번더 진행. DP(N//3) + N % 3 : 3으로 나누어지게 숫자를 추가해서 만드냐,  DP(N//2) + N % 2 : 2로 나누어지게 만드는 최소 횟수 구하기
    cnt = 1 + min(DP(N//3) + N % 3, DP(N//2) + N % 2)
    memo[N] = cnt # 메모제이션
    return cnt
print(DP(N))
