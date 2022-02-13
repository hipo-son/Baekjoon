import sys # https://study-all-night.tistory.com/5
input = sys.stdin.readline
import numpy as np

N = int(input().rstrip())

Map = [[0 for i in range(N)] for i in range(N)]  # 배열 생성

def draw_star(n) :
    global Map # 전체 배열 가져옴

    if n == 3 :# 3일떄의 map 형성
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return

    a = n//3 # 3이 아닐때 임시 작은 셀
    draw_star(n//3) # 작은셀의 함수 아 !!! 조건을 맞추어 위의 if 를 먼저 건들인다.

    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            for k in range(a) : # 3일떄 9일때 생각
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] #????

                # print(Map[k][:a])

draw_star(N) # 함수

# for i in Map : # 0 false, 1 True
#     for j in i :
#         if j :
#             print('*', end = '')
#         else :
#             print(' ', end = '')
#     print()
