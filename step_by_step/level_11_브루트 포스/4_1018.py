import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
size = 8
board = []
for i in range(N): # 문자를 리스트로 받음
    tmp = list(map(str ,input().rstrip()))
    board.append(tmp)

list = []
for i in range(len(board)-(size-1)):  # 원하는 크기만큼 색일할 위치를 표현
    for j in range(len(board[i])-(size-1)):
        list.append([i,j]) # 시작할 위치들 리스트로 표현

total = []
for happy in list:
    # print(happy)
    count = 0
    for i in range(happy[0], happy[0] + size):
        for j in range(happy[1], happy[1] + size):
            if board[i][j] == 'W' and (i + j) % 2 == 0:
                continue
            elif board[i][j] == 'B' and (i + j) % 2 == 1:
                continue
            else:
                count +=1
    total.append(count)
print(min(total))
