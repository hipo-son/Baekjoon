import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
six_n = 666
while True:
    if '666' in str(six_n): # 단어가 있을때 카운트
        cnt += 1
    if cnt == n: # 반복수
        print(six_n)
        break
    six_n += 1
