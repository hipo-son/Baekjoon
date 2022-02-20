import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
num = list(map(int, input().rstrip().split()))
num.sort()
result = []
Li = []

def dfs(start):
    if len(Li) == M:
        tmp = []
        for i in Li:
            tmp.append(num[i])
        result.append(tuple(tmp))
        return

    for i in range(0, N):
            Li.append(i)
            dfs(i)
            Li.pop()
dfs(0)

result = sorted(list(set(result)))
for i in result:
    print(*i)
