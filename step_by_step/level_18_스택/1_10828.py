import sys
input = sys.stdin.readline
N = int(input())

stack=[]
for i in range(N):
    command = input().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if not stack: #  if len(stack)==0: 같은 뜻
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
#########################################################

# import sys
# input = sys.stdin.readline
# N = int(input())
#
# stack=[]
# for i in range(N):
#     command = input().split()
#
#     if command[0]=='push':
#         stack.append(command[1])
#     elif command[0]=='pop':
#         if len(stack)==0:
#             print(-1)
#         else:
#             print(stack.pop())
#     elif command[0] == 'size':
#         print(len(stack))
#     elif command[0] == 'empty':
#         if len(stack)==0:
#             print(1)
#         else:
#             print(0)
#     elif command[0] == 'top':
#         if len(stack)==0:
#             print(-1)
#         else:
#             print(stack[-1])
