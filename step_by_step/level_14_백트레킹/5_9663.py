import sys
input = sys.stdin.readline

N = int(input().rstrip())
a, b, c = [False]*N, [False]*(2*N-1), [False]*(2*N-1) # 수직, 우상향, 좌상향
result = 0
def solve(i):
    global result

    if i == N:
        result += 1
        return

    for j in range(N): # 열 좌표
        if not (a[j] or b[i+j] or c[i-j+N-1]): # 수직, 우상향, 좌상향 해당사항 조사
            a[j] = b[i+j] = c[i-j+N-1] = True
            solve(i+1) # 다음 행으로 재귀
            a[j] = b[i+j] = c[i-j+N-1] = False

solve(0)
print(result)

##############################################################
#
# N = int(input().rstrip())
# Li = [None for _ in range(N)]
# set_Li, rightward, leftward = set([]), set([]), set([])
# result = 0
#
# def f(start):
#     global result
#     if len(set_Li) ==  N:
#         result += 1
#         print(Li)
#         return
#     for i in range(start, N):
#         if Li[i] == None :
#             for j in range(0, N):
#                 if j not in set_Li and (i+j) not in rightward and (i-j) not in leftward:
#                     Li[i] = j
#                     set_Li.add(j)
#                     rightward.add(i+j)
#                     leftward.add(i-j)
#                     f(start + 1)
#                     Li[i] = None
#                     set_Li.remove(j)
#                     rightward.remove(i+j)
#                     leftward.remove(i-j)
# f(0)
# print(result)
