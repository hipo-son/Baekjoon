import sys
input = sys.stdin.readline

while True: # EOF 파이썬 예외 처리 try, except 사용
    try:
        A, B = map(int, input().rstrip().split())
        print(A + B)
    except:
        break
