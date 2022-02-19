import sys
input = sys.stdin.readline

Li = [list(map(int, input().rstrip().split())) for i in range(9)] #리스트
zeros = [(i, j) for i in range(9) for j in range(9) if Li[i][j] == 0] # 0인 좌표


def rows(x, num): # 숫자가 있을 경우 T 없을경우 F
    if num in Li[x]:
        return True
    return False

def cols(y, num):
    for i in range(9):
        if num == Li[i][y]:
            return True
    return False

def box(x, y, num):
    xx = x // 3
    yy = y // 3
    for i in range(3):
        for j in range(3):
            if num == Li[xx*3 + i][yy*3 + j]:
                return True
    return False

def DFS(idx):
    if len(zeros) == idx: # 0인 좌표들에 값을 모두 넣어주면
        for _ in Li:
            print(*_)
        sys.exit()

    for num in range(1, 10): # 1부터 9까지
        x, y = zeros[idx][0], zeros[idx][1]  # 0인 좌표 의 x, y

        if not (rows(x, num) or cols(y, num) or box(x, y, num)): # 숫자가 없는경우
            Li[x][y] = num
            DFS(idx +1)
            Li[x][y] = 0

DFS(0)
