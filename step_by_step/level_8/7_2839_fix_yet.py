import sys
input = sys.stdin.readline

n = int(input().rstrip())

count = 0
remainder = (n % 30)
n_3 = list(range(3,60,5)) + list(range(6,60,5)) + list(range(9,60,5)) + list(range(12,60,5)) + list(range(0,60,5))
n_3_defult = list(range(3,30,5)) + list(range(6,30,5)) + list(range(9,30,5)) + list(range(12,30,5)) + list(range(0,30,5))
n_3_list = list(map(lambda x: (x % 30), n_3))

if n in set(n_3_list)-set(n_3_defult):
    count = -1
else:
    count += (n // 30) * 6
    if n % 5 == 0: # 5 만 있을때
        count += remainder // 5
    elif n % 5 == 1: # 3이 2개
        count += 2
        count += (remainder - 6) // 5
    elif n % 5 == 2: # 3이 4개
        count += 4
        count += (remainder - 12) // 5
    elif n % 5 == 3: # 3이 1개
        count += 1
        count += (remainder - 3) // 5
    elif n % 5 == 4: # 3이 3개
        count += 3
        count += (remainder - 9) // 5

print(count)
############################### fix
