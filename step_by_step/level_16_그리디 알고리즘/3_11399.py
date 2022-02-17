import sys
input = sys.stdin.readline

N = int(input().rstrip())
Li = list(map(int, input().rstrip().split()))

Li.sort()

total = 0
sum = 0
for i in Li:
    sum += i
    total += sum

print(total)
