import sys
input = sys.stdin.readline
A ,B, V = list(map(int, input().rstrip().split()))

day = (V - A) // (A - B) + 2 # 기준 m 를 넘어가는경우
if (V - A) % (A - B) == 0:  # 딱 떨어지는 경우
    day -= 1
print(day)

###################
print((V-B-1) // (A-B) + 1) # 가능
