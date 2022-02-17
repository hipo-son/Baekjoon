import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

s = []
def f():
  if len(s) == M: # 2 : 길이가 만족될때 출력
    print(' '.join(map(str, s))) # .join 함수 알기
    return

  for i in range(1, N + 1): # 1
    if i in s: # 있는 숫자 pass
      continue
    s.append(i) # 1 : 없는 숫자 추가
    f() # 1.5 , 2
    s.pop() # 3 : 출력후 이전 숫자 제거

f()
########################################
# def f(s):
#   if len(s) == M:
#     print(' '.join(map(str, s)))
#     return
#
#   for i in range(1, N + 1):
#     if i in s:
#       continue
#     f(s + [i])
#
# f([])
