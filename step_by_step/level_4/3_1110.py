import sys
input = sys.stdin.readline

cycle = 0
num = input().rstrip()
tmp = int(num)

while True:
    cycle += 1
    if tmp < 10:
        tmp = '0' + str(tmp)[0]
    sum = int(str(tmp)[0]) + int(str(tmp)[-1])
    # print(int(str(tmp)[0]) , int(str(tmp)[-1]), end = ' ')  # 확인 용도
    tmp = int(str(tmp)[-1] + str(sum)[-1])
    # print(sum, tmp)  # 확인 용도

    if tmp == int(num):
        break
        
print(cycle)
