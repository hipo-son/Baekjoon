import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
result = list(map(int, input().rstrip().split()))
result.sort()
Li = []

def dfs(start):
    if len(Li) == M:
        for i in Li:
            print(result[i], end =' ')
        print()
        return

    for i in range(start, N):
        if i not in Li:
            Li.append(i)
            dfs(i+1)
            Li.pop()
dfs(0)
