import sys
input = sys.stdin.readline

memo = {}
def w(a, b, c):
    if (a, b, c) in memo:
        return memo[(a, b, c)]

    elif a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    elif a < b and b < c:
        tmp = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        memo[(a, b, c)] = tmp
        return tmp

    else:
        tmp = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        memo[(a, b, c)] = tmp
        return tmp

while True:
    a, b, c = map(int, input().rstrip().split())
    if a == b == c == -1 :
        break
    else:
        print('w({0}, {1}, {2}) = {3}'.format(a, b, c, w(a, b, c)))
