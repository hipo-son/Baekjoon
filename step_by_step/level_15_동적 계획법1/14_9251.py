import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

DP = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)] # i, j 의 DP를 i+1, j+1에 저장

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]: # 같은 글자 일때
            DP[i+1][j+1] = DP[i][j] + 1
        else: # 같이 않을때 주어진 문자의 최대를 저장
            DP[i+1][j+1] = max(DP[i][j+1], DP[i+1][j])
print(DP[-1][-1])
