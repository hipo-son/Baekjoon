import sys
input = sys.stdin.readline

N = int(input().rstrip())
Li = [list(map(int, input().rstrip().split())) for i in range(N)]
M = int(N/2)
start_team = []
result = []
def DFS(dth): # 계산 해야될 사람 배열 start team
    if len(result) == M:
        start_team.append(list(result)) # [1,2,3]
        return

    for i in range(dth, N+1):
        if i not in result:
            result.append(i)
            DFS(i+1)
            result.pop()
DFS(1)

index = []
for i in range(0, M):
    for j in range(i+1, M):
        index.append([i,j])
num = [i for i in range(1, N+1)]

total = []
for _ in start_team:
    link_team = list(set(num) - set(_))
    table1, table2 = 0, 0
    for i in index:
        table1 += Li[_[i[0]]-1][_[i[1]]-1] + Li[_[i[1]]-1][_[i[0]]-1]
        table2 += Li[link_team[i[0]]-1][link_team[i[1]]-1] + Li[link_team[i[1]]-1][link_team[i[0]]-1]
    tmp = abs(table1 - table2)
    total.append(tmp)
print(min(list(total)))

# print(min(total))
##################################################
# from itertools import combinations
# members = [i for i in range(N)]
# possible_team = []
#
# #조합으로 가능한 팀 생성해주기
# for team in list(combinations(members, N//2)):
#     possible_team.append(team)
# print(possible_team)
# # 3인 이상인 팀일때 다시 2명씩 만들기
#
# # 12, 34 구현후 합















# ######################################################### 메모리 초과 ;;;;
# from itertools import permutations
# N = int(input().rstrip())
# M = int(N/2)
# stat = [input().rstrip().split() for i in range(N)]
#
# Li, total = [], []
# def f(idx):
#     if len(Li) == M:
#         total.append(list(Li))
#         return
#
#     for i in range(idx, N+1):
#         if i not in Li:
#             Li.append(i)
#             f(idx +1)
#             Li.pop()
# f(1)
# num = [i for i in range(1, N+1)]
# result = []
# for i in range(len(total)):
#     start = total[i]
#     link = list(set(num) - set(start))
#     start_per = list(permutations(start, 2))
#     link_per = list(permutations(link, 2))
#     start_list, link_list = [], []
#     for j in range(len(start_per)):
#         tmp1 = stat[start_per[j][0] -1][start_per[j][1] -1]
#         tmp2 = stat[link_per[j][0] -1][link_per[j][1] -1]
#         start_list.append(int(tmp1))
#         link_list.append(int(tmp2))
#     result.append(abs(sum(start_list) - sum(link_list)))
# print(min(result))
