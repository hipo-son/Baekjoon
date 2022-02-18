import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Li = []

def dfs():
    if len(Li) == M:
        print(' '.join(map(str, Li)))
        return

    for i in range(1, N+1):
            Li.append(i)
            dfs()
            Li.pop()
dfs()
