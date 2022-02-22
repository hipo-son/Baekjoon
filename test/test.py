import sys
input = sys.stdin.readline

N = int(input().rstrip())

def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

if N == 0:
    print('0')
else:
    print(fibo(N))
