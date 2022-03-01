import sys #유클리드 호재법
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

num = int(input())

for i in range(num):
  a, b = map(int, input().split())
  print(lcm(a, b))
