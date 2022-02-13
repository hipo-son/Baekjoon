import sys
input = sys.stdin.readline

C = int(input().rstrip())

for i in range(C):
    tmp = list(map(int, input().rstrip().split()))
    mean = (sum(tmp[1:]) / tmp[0])
    high_score = [x for x in tmp[1:] if x > mean ]
    result = ((len(high_score) / tmp[0]) * 100 )
    print('{:.3f}%'.format(result))
