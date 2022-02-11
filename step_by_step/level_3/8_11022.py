import sys
input = sys.stdin.readline

num = int(input().rstrip())

for i in range(1, num + 1):
    tmp = input().rstrip().split()
    print("Case #{0}: {1} + {2} = {3}".format(i, int(tmp[0]), int(tmp[1]), (int(tmp[0]) + int(tmp[1]))))
