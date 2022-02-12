import sys
input = sys.stdin.readline
xy1 = list(map(int, input().rstrip().split()))
xy2 = list(map(int, input().rstrip().split()))
xy3 = list(map(int, input().rstrip().split()))

result = [0,0]
for i in range(0,2):
    if xy1[i] == xy2[i]:
        result[i] = xy3[i]
    elif xy1[i] == xy3[i]:
        result[i] = xy2[i]
    elif xy2[i] == xy3[i]:
        result[i] = xy1[i]
print(result[0], result[1])
############################## 함수로 정의해서 해도 괜찮을듯
