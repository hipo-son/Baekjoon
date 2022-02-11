import sys
input = sys.stdin.readline

S = input().rstrip()
tmp = 'abcdefghijklmnopqrstuvwxyz'
for i in tmp:
    print(S.find(i) ,end = " ") # find 함수 사용
