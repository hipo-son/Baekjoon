import sys
input = sys.stdin.readline
tmp = list(map(int, input().rstrip().split()))

if tmp[1] >= tmp[2]:
    result = -1
elif tmp[0] + tmp[1] < tmp[2]:
    result = 1
else:
    diff = tmp[2] - tmp[1]
    result = (tmp[0] // diff) + 1

print(result)
