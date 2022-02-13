import sys
input = sys.stdin.readline

num = input().rstrip()
tmp = list(map(int, input().rstrip().split()))

print(min(tmp), max(tmp))
