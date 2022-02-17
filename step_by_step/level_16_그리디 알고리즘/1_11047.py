import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
Li = [int(input().rstrip()) for _ in range(N)]

Li.reverse() # 큰 순서대로
cnt = 0

for i in Li:
    if M >= i : # 나눌수 있는 수는 빼준다
        cnt += M // i
        M %= i
print(cnt)
