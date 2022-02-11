import sys
input = sys.stdin.readline

while True:
    try:
        A, B = map(int, input().rstrip().split())
        print(A + B)
    except:
        break
