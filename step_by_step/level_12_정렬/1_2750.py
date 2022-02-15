import sys
input = sys.stdin.readline

N = int(input().rstrip())
num_list = []
for i in range(N):
    num = int(input().rstrip())
    num_list.append(num)

num_list.sort()

for i in num_list:
    print(i)
