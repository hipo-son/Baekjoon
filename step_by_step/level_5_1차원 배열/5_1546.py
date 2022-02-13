import sys
input = sys.stdin.readline

N = input().rstrip()
tmp = list(map(int, input().rstrip().split()))

M = max(tmp)
def function(x):
    return x / M * 100

tmp = list(map(function, tmp ))
print(sum(tmp) / len(tmp))
