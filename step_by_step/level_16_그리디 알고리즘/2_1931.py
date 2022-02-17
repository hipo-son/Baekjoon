import sys
input = sys.stdin.readline

N = int(input().rstrip())
Li = []
for i in range(N):
    a, b = map(int, input().rstrip().split())
    Li.append([a, b])

Li.sort(key = lambda a: a[0])
Li.sort(key = lambda a: a[1])

cnt , last = 0, 0
print(Li)
for i, j in Li:
    if i >= last:
        cnt += 1
        last = j

print(cnt)
