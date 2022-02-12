import sys
input = sys.stdin.readline
T = int(input().rstrip())
for i in range(T):
    x, y = map(int, input().rstrip().split())
    distance = y - x
    count, total, tmp = 0, 0, 0
    i = 1
    while distance > total:
        if tmp == 1:
            tmp = 0
            total += i
            i += 1
        else:
            tmp += 1
            total += i
        count += 1
    print(count)
