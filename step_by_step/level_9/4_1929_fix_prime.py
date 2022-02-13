import sys
input = sys.stdin.readline
M, N = map(int, input().rstrip().split())

for i in range(M, N+1):
    if i == 1: #1은 소수 X
        continue
    for j in range(2, int(i ** 0.5)+1 ): # 약수 판별 : 약수 판별시 모든수를 대입해 보는것 보다 제곱근을 이용해서 구하는게 빠르다. 이유: 보통 12의 약수 1,2,3,4,6,12 일떄 1*12, 2*6, 3*4 이렇게 이뤄졌으므로 
        if i%j==0:
            break
    else:
        print(i)
################################
