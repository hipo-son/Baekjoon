import sys

def hanoi(num, f, b, t):
    if num == 1:
        print(f, t)
    else:
        hanoi(num-1, f, t, b)
        print(f, t)
        hanoi(num-1, b, f, t)

num = int(sys.stdin.readline())
print(2**num - 1)
hanoi(num, 1, 2, 3)
