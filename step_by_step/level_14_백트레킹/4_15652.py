import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Li = []

def dfs(start):
    if len(Li) == M:
        print(' '.join(map(str, Li)))
        return

    for i in range(start, N+1):
        Li.append(i)
        dfs(i)
        Li.pop()

dfs(1)
