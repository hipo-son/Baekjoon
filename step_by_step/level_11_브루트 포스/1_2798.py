import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

card = list(map(int,input().rstrip().split()))

list = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] <= M:
                sum = card[i] + card[j] + card[k]
                list.append(sum)
print(max(list))
