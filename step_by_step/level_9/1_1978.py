import sys
input = sys.stdin.readline

def primenumber(x): # 소수 판별 함수
    for i in range(2, x):
    	if x % i == 0:
        	return False
    return True
count = 0

N = int(input().rstrip())
tmp = list(map(int,input().rstrip().split()))

if 1 in tmp:
    count -= 1
tmp = list(map(primenumber,tmp))
count += tmp.count(True)
print(count)
