import sys
input = sys.stdin.readline
from collections import Counter

N = int(input().rstrip())
L = []

for _ in range(N):
    L.append(int(input().rstrip()))

print(round(sum(L) / N)) # 평균 계산후 반올림

L.sort()
print(L[N//2])  #조건에서 홀수이므로

cnt_L = Counter(L).most_common()
if len(cnt_L) > 1 and cnt_L[0][1]==cnt_L[1][1]: #최빈값 2개 이상일때
    print(cnt_L[1][0])
else: # 리스트 숫자가 하나일때
    print(cnt_L[0][0])

print(max(L)-min(L))
