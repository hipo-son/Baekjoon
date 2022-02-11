S = int(input())

for i in range(S):
    tmp = input().split()
    for i in tmp[1]:
        print(int(tmp[0]) * i, end="")
    print() # 줄바꿈
