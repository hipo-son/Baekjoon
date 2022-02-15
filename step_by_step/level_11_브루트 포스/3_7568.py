import sys
input = sys.stdin.readline

N = int(input().rstrip())

list = []
for i in range(N):
    x, y = map(int, input().rstrip().split())
    list.append([x,y])

for i in range(N):
    rank = 1
    for j in range(N):
        if list[i][0] < list[j][0] and list[i][1] < list[j][1]:
            rank += 1
    print(rank, end=' ')
