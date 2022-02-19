import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input().rstrip())
M = int(N/2)
stat = [input().rstrip().split() for i in range(N)]

Li, total = [], []
def f(idx):
    if len(Li) == M:
        total.append(list(Li))
        return

    for i in range(idx, N+1):
        if i not in Li:
            Li.append(i)
            f(idx +1)
            Li.pop()
f(1)

total_1 = []
for i in total:
    tmp = []
    for j in i:
        tmp.append((N + 1) - j)
    # if tmp in total: # 오히려 시간이 많이듬
    #     total.remove(tmp)
    total_1.append(tmp)

result = []
for i in range(0, len(total)):
    tmp1 = list(permutations(total[i], 2))
    tmp2 = list(permutations(total_1[i], 2))
    tmp1_list = []
    tmp2_list = []
    for j in range(0, len(tmp1)):
        tmp1_list.append(int(stat[tmp1[j][0] - 1][tmp1[j][1] - 1 ]))
        tmp2_list.append(int(stat[tmp2[j][0] - 1][tmp2[j][1] - 1 ]))
    result.append(abs(sum(tmp1_list)-sum(tmp2_list)))
print(result)
print(min(result))
