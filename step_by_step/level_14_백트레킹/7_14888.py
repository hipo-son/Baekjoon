import sys
input = sys.stdin.readline

N = int(input().rstrip())
Li = list(map(int, input().rstrip().split()))
plus, minus, multiply, division = map(int, input().rstrip().split())
total = [] # 될 수있는 합들의 리스트

def DFS(idx, result, plus, minus, multiply, division): # 인자
    if idx == N :
        total.append(result)
        return

    if plus:
        DFS(idx +1, result + Li[idx] ,plus-1, minus, multiply, division)
    if minus:
        DFS(idx +1, result - Li[idx] ,plus, minus-1, multiply, division)
    if multiply:
        DFS(idx +1, result * Li[idx], plus, minus, multiply-1, division)
    if division:
        DFS(idx +1, int(result / Li[idx]), plus, minus, multiply, division-1)

DFS(1, Li[0], plus, minus, multiply, division)
print(max(total))
print(min(total))
