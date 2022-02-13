import sys
input = sys.stdin.readline

num = int(input().rstrip())

for i in range(num):
    tmp = input().rstrip() #문자
    tmp_len = len(tmp)
    score = 0
    plus_score = 1
    for i in range(0,tmp_len):
        if tmp[i] == 'O':
            score += plus_score
            plus_score += 1
        elif tmp[i] == 'X':
            plus_score = 1
    print(score)
