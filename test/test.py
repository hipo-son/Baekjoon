from math import factorial

N, K = 26, 5

result = factorial(N)//(factorial(K) * factorial(N-K))

print(result)
# 전체 / 내패 , 바퀴수
