import sys
input = sys.stdin.readline

N = int(input().rstrip())

L = []
for i in range(N):
    L.append(list(input().rstrip().split()))

L.sort(key = lambda x:int(x[0])) # 나이만 정렬, 이름은 입력순

for i in range(N):
    print(L[i][0], L[i][1])
