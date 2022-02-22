import sys
input = sys.stdin.readline

def fib(n):
        f0, f1 = 0, 1
        f = [1] * n
        for i in range(1,n):
            f[i] = f0 + f1
            f0 , f1 = f1, f[i]
        return f
n = int(input().rstrip())
if n == 0:
    print(0)
else:
    print(fib(n)[n-1])
######################################
import sys
input = sys.stdin.readline

N = int(input().rstrip())

def fibo(x):
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
print(fibo(N))
