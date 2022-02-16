import sys
input = sys.stdin.readline

N = int(input().rstrip())

L = list(map(int, input().rstrip().split())) # 리스트 만들기

L_1 = sorted(list(set(L))) # set 으로 중복 제거, 오름차순 정렬
dic = {L_1[i] : i for i in range(len(L_1)) } # 딕셔너리 만듬 , index를 value로

for i in L: # 입력맏은 값의 value 출력
    print(dic[i] , end=' ')
