import sys
input = sys.stdin.readline

N = int(input().rstrip())

for i in range(1, N+1):
    num = sum((map(int, str(i)))) # 각 자리수 합
    num_sum = i + num

    if num_sum == N:
        print(i)
        break

    if i == N:
        print(0)
