import sys
input = sys.stdin.readline

A, B, C = int(input().rstrip()), int(input().rstrip()), int(input().rstrip())

total = A * B * C
total = list(map(int,str(total))) # 문자 하나 하나 리스트 만들기
for i in range(0, 10):
    print(total.count(i))
