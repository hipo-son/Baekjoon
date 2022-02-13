import sys
input = sys.stdin.readline
import math

T = int(input().rstrip())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().rstrip().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2) # 두 원의 거리
    if distance == 0 and r1 == r2 : # 합동
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance: # 내접, 외점 원
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) : # 교점이 두개일때
        print(2)
    else: # 접하지 않을때
        print(0)
