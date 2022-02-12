import sys
input = sys.stdin.readline
T = int(input().rstrip())

for i in range(T):
    H ,W, N = map(int, input().rstrip().split())

    YY = N % H
    if YY == 0: # 꼭대기 층 일떄
        YY = H

    XX = N // H + 1
    if N % H == 0: # 꼭대기 층 일때
        XX -= 1
    print('%d%02d'%(YY,XX))
