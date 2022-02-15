import sys
input = sys.stdin.readline

N = int(input().rstrip())
L = []
for i in range(N):
    ab = list(map(int, input().rstrip().split()))
    L.append(ab)
L.sort()

for i in L:
    print(i[0], i[1])
