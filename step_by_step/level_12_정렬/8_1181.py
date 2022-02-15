import sys
input = sys.stdin.readline

N = int(input().rstrip())
L = []
for _ in range(N):
    word = input().rstrip()
    L.append(word)

L = list(set(L))
L.sort()
L.sort(key = len)
for i in L:
    print(i)
