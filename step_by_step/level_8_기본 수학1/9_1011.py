import sys
input = sys.stdin.readline
T = int(input().rstrip())
for i in range(T):
    x, y = map(int, input().rstrip().split())
    distance = y - x   # 좌표간 거리
    count, total, tmp = 0, 0, 0
    i = 1
    while distance > total: # 공간이동시 가장 멀리 갈수 있는 total 계산 
        if tmp == 1:
            tmp = 0
            total += i
            i += 1
        else:
            tmp += 1
            total += i
        count += 1
    print(count)
