import sys
input = sys.stdin.readline

tmp = input().rstrip().split()
if int(tmp[0][::-1]) < int(tmp[1][::-1]):
    print(int(tmp[1][::-1]))
else:
    print(int(tmp[0][::-1]))
