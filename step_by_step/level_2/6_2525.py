import sys
input = sys.stdin.readline
H, M = map(int, input().rstrip().split())
time = int(input().rstrip())

M += time

while M >= 60:
    H += 1
    M -= 60
    if H >= 24:
        H -= 24
print(H, M)
