import sys
input = sys.stdin.readline

def factorial(x):
    result = 1
    for i in range(1,x + 1):
        result *= i
    return result

N = int(input().rstrip())

print(factorial(N))
