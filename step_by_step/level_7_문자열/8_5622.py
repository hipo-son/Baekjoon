import sys
input = sys.stdin.readline

word = list(input().rstrip())

alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
total_time = 0
for i in word: # 처음 단어 리스트
    for j in alphabet: # alphabet 각 원소 문자
        if i in j:
            total_time += (alphabet.index(j) + 3)
print(total_time)
