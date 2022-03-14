import sys
input = sys.stdin.readline

N = int(input())
stack, Li = [], []
count = 1; temp = 1
for i in range(N):
    num = int(input())
    while count <= num:
        stack.append(count)
        Li.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        Li.append('-')
    else:
        temp = 0

if not temp:
    print('NO')
else:
    for _ in Li:
        print(_)
