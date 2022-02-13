import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split()) # map 함수 (function, iterable : list etc) # map 결과물 :iterator
C = list(map(int, input().split()))

result = []
for i in range(A):
    if C[i] < B:
        print(C[i], end = ' ') # end : 다음 번 출력이 /n 대신 지정한 값이 됨
    
