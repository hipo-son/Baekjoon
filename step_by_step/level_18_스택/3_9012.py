import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    string = input()
    stack = []
    for _ in string:
        if _ == '(':
            stack.append('(')
        elif _ == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                print('NO')
                break
        elif not len(stack):
            print('YES')
            break
        else:
            print('NO')
            break
