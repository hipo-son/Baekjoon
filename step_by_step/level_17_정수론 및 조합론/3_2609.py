import sys #유클리드 호재법
input = sys.stdin.readline
a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))
#############################
#import math
#
#a, b = map(int, input().split())
#
#print(math.gcd(a, b))
#print(math.lcm(a, b))
