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
num = [i for i in range(1, N+1)]
result = []
for i in range(len(total)):
    start = total[i]
    link = list(set(num) - set(start))
    start_per = list(permutations(start, 2))
    link_per = list(permutations(link, 2))
    start_list, link_list = [], []
    for j in range(len(start_per)):
        tmp1 = stat[start_per[j][0] -1][start_per[j][1] -1]
        tmp2 = stat[link_per[j][0] -1][link_per[j][1] -1]
        start_list.append(int(tmp1))
        link_list.append(int(tmp2))
    result.append(abs(sum(start_list) - sum(link_list)))
print(min(result))
######################################################### 메모리 초과 ;;;;
