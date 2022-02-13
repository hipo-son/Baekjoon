import sys
input = sys.stdin.readline # 느린 파이썬의 입출력 해곃책

num = int(input().rstrip())  # 개행문자 제외 문자열만 출력 하기 위해서

for i in range(0,num):
    tmp = input().rstrip().split()
    print(int(tmp[0]) + int(tmp[1]))
