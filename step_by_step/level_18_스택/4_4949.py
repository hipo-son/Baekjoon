import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break
    stack = []
    for _ in s:
        if _ not in '()[]':
            continue
        if _ == '(' or _ == '[':
            stack.append(_)
        elif ( _ == ')' and stack and stack[-1] == '(' ) or ( _ == ']' and stack and stack[-1] == '[' ):
            stack.pop()
        else:
            stack.append(0) # false
            break
    print('no' if stack else 'yes')
