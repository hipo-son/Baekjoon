import sys
input = sys.stdin.readline

N = int(input())
Li = []
for i in range(N):
    num = int(input())
    if num == 0:
        Li.pop()
    else:
        Li.append(num)
print(sum(Li))
