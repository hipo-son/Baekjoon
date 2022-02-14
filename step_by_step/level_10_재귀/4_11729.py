import sys
input = sys.stdin.readline

N = int(input().rstrip())

def hanoi(N, f, b, t):
    if N == 1:
        print(f, t) # 시작 > 목표지점
    else:
        hanoi(N-1, f, t, b) # 가장 밑에 원반 제외후 이동 # f > t 가 f > b 로 이동한다.
        print(f, t) # 가장 큰 원반 이동
        hanoi(N-1, b, f, t) # b에 쌓여 있던 원반을 t로 다 이동

print(2**N - 1)
hanoi(N, 1, 2, 3)
