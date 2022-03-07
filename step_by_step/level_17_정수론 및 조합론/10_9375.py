import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    M = int(input())
    dic = {}
    for j in range(M):
        Li = input().split()
        if Li[1] in dic: # 같은 종류의 옷이 있으면 추가
            dic[Li[1]].append(Li[0])
        else:
            dic[Li[1]] = [Li[0]]
    total = 1
    for k in dic: # 옷의 종류
        total *= (len(dic[k]) + 1) # +1 의 경우 안입을경우 생각
    print(total -1) # 다 안입는경우
