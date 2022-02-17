import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
visited = [False] * N
Li = []

def f(depth):
    if len(Li) == M:
        print(' '.join(map(str, Li)))
        return

    for i in range(visited):
        if not visited[i]:
            visited[i] = True
            Li.append(i + 1)
            f(depth + 1)
            visited[i] = False
            Li.pop()
f(0)
