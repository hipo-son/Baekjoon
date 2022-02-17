import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
Li = [int(input().rstrip()) for _ in range(N)]

Li.reverse()
cnt = 0

for i in Li:
    if M >= i :
        cnt += M // i
        M %= i
print(cnt)
