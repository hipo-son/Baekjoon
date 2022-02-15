import sys
input = sys.stdin.readline

N = int(input().rstrip())
num_list = []
for i in range(N):
    num_list.append(int(input().rstrip()))

num_list.sort()

for i in num_list:
    print(i)
