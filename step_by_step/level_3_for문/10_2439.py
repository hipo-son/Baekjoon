import sys
input = sys.stdin.readline

num = int(input().rstrip())

for i in range(1, num+1):
    print(' ' * (num - i) + '*' * i)
