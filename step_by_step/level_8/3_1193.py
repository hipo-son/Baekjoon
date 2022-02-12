import sys
input = sys.stdin.readline
num = int(input().rstrip())

i = 1
def sigma(x):
    return int(((i + 1 ) * i) / 2)   # sigma 를 이용해 (n / 1) 찾기
while True:
    if i % 2 == 0 and sigma(i) >= num: # 대각선이 짝수 줄 일때
        n = [ i - (sigma(i)-num) , 1 + (sigma(i)-num) ]
        break
    if i % 2 == 1 and sigma(i) >= num: # 대각선이 홀수 줄 일때
        n = [  1 + (sigma(i)-num) , i - (sigma(i)-num) ]
        break
    else:
        i += 1
print("{0}/{1}".format(n[0],n[1]))
