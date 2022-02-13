import sys
input = sys.stdin.readline

def sum_underfloor(x):
    result = 0
    for j in range(0, x +1):
        result += n_n[j]
    return result

T = int(input().rstrip())

for i in range(T):
    k, n = int(input().rstrip()), int(input().rstrip())

    n_n =[i for i in range(1, 15)] # 0층 주민 수

    for floor in range(1, k + 1): # k 층 주민 수 
        n_n = list(map(sum_underfloor, range(0,14)))
    print(n_n[n-1])
