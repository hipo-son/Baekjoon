import sys
input = sys.stdin.readline
from collections import Counter # 데이터의 개수 카운팅시 사용하는 모듈
while True: # 굳이 예외는 안해도 됬음 , 런타임 떠서 시도해봤음
    try:
        word = input().rstrip().upper() # 대문자 변환
        list = Counter(word).most_common()
        if len(list) == 1:
            print(list[0][0])
        else:
            if list[0][1] == list[1][1] or len(list) == 1:
                print('?')
            else:
                print(list[0][0])
    except:
        break
