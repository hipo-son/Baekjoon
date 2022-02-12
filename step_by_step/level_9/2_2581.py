import sys
input = sys.stdin.readline

def primenumber(x): # 소수 출력 함수, 소수가 아닐시 None 출력
    if x == 1:
        return None
    else:
        for i in range(2, x):
            if x % i == 0:
                return None
        return x

M, N = int(input().rstrip()), int(input().rstrip())
list = list(map(primenumber, range(M,N+1)))
list = [i for i in list if i not in {None}] # None 제거
if list == []:
    print('-1')
else:
    print(sum(list))
    print(min(list))
