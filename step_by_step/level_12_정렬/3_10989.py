import sys
input = sys.stdin.readline

N = int(input().rstrip())

num = [0] * 10001 # num이 일정한 범위의 특수한경우 지정된 수의 개수를 저장하면 메모리를 효율적으로 사용가능

for i in range(N):
    tmp = int(input().rstrip())
    num[tmp] += 1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)
