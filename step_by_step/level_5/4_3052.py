import sys
input = sys.stdin.readline

total= []
for i in range(10):
    num = input().rstrip()
    total.append(int(num) % 42)
total = list(set(total)) # set 사용시 중복값 제거
print(len(total))
