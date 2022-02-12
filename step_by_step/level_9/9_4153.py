import sys
input = sys.stdin.readline

while True:
    tmp = list(map(int, input().rstrip().split()))
    if tmp == [0, 0, 0]:
        print()
        break
    top = int(max(tmp))
    tmp.remove(top)
    if top**2 == (tmp[0]**2 + tmp[1]**2):
        print('right')
    else:
        print('wrong')
