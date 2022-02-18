import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Li = []

def dfs(start):
    if len(Li) == M:
        print(' '.join(map(str, Li)))
        return

    for i in range(start, N+1):
        if i not in Li:
            Li.append(i)
            dfs(i+1)
            Li.pop()
dfs(1)
