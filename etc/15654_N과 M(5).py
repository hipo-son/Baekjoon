import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
Li = list(map(int, input().rstrip().split()))

Li.sort()
result = []
def DFS(idx):
    if idx == M:
        print(*result)
        return

    for i in Li:
        if i not in result:
            result.append(i)
            DFS(idx +1)
            result.pop()

DFS(0)
