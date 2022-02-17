import sys
input = sys.stdin.readline

N = int(input().rstrip())
road = list(map(int, input().rstrip().split()))
city = list(map(int, input().rstrip().split()))

total = 0 # 총비용
min_oil = city[0] #처음 비용
for i in range(N-1):
    if city[i] <= min_oil: #도시의 기름값이 최소인가?
        min_oil = city[i]
    total += road[i] * min_oil # 해당도시와 다음도시의 거리 

print(total)
