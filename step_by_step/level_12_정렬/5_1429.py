import sys
input = sys.stdin.readline

N = list(map(int,input().rstrip()))

N.sort()
N.reverse()

for i in N:
    print(i,end="")
