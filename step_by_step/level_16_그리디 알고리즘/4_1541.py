import sys
input = sys.stdin.readline

Li = list(input().rstrip().split('-'))

total = 0

for i in Li[0].split('+'): # 첫번째항은 무조건 양수이므로
    total += int(i)

for i in Li[1:]: # 최소가 될라면 - 뒤에는 () 로 묶어 계산해야한다.
    for j in i.split('+'):
        total -= int(j)

print(total)
