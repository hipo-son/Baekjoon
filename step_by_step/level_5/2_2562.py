import sys
input = sys.stdin.readline

tmp = []
for i in range(9):
    num = input().rstrip()
    tmp.append(num)

tmp = list(map(int, tmp))

max_value = max(tmp)
print(max_value)
print(int(tmp.index(max_value)) + 1)
