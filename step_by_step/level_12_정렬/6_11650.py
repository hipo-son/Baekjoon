import sys
input = sys.stdin.readline

N = int(input().rstrip())
L = []
for i in range(N):
    a, b = map(int, input().rstrip().split()))
    L.append([a, b])
L.sort()

for i in L:
    print(i[0], i[1])
