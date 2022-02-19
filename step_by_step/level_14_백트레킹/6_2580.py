import sys
input = sys.stdin.readline
import numpy as np


Li = [list(map(int, input().rstrip().split())) for i in range(9)]































################################################################# fail
# num = [i for i in range(1, 10)]
# tmp = [[] for i in range(9)]
# row = [tmp for i in range(9)]
# col = [tmp for i in range(9)]
# print()
# def rows(x) :
#     tmp = set(num)
#     for i in range(9) :
#         tmp -= set([Li[x][i]])
#     if len(tmp) != 0 :
#         return list(tmp)
#     else:
#         return []
#
# def cols(x) :
#     tmp = set(num)
#     for j in range(9) :
#         tmp -= set([Li[j][x]])
#     if len(tmp) != 0 :
#         return list(tmp)
#     else:
#         return []
#
# for i in range(9):
#     for j in range(9):
#         if Li[i][j] == 0: # 해당 좌표가 0일때
#             row[i][j] = rows(i)
#             col[i][j] = cols(j)
#
# print(row)
# print(col)
