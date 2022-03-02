import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))

up, down = 1, 1

for i in range(N, N-K, -1):
    up *= i

for i in range(1, K+1):
    down *= i

print(up // down)
################################
# from math import factorial
#
# N, K = list(map(int, input().split()))
#
# print(factorial(N)//(factorial(K) * factorial(N-K)))
