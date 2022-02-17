import sys
input = sys.stdin.readline

N = int(input().rstrip())
road = list(map(int, input().rstrip().split()))
city = list(map(int, input().rstrip().split()))

total = 0
min_oil = city[0]
for i in range(N-1):
    if city[i] <= min_oil:
        min_oil = city[i]
    total += road[i] * min_oil

print(total)
