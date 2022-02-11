import sys
input = sys.stdin.readline
num = int(input().rstrip())
i, total = 1, 1
while True:
    if total < num:
        total += (i * 6)
        i += 1
    else:
        print(i)
        break
