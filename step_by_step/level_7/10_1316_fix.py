import sys
input = sys.stdin.readline
from collections import Counter

count = 0
N = int(input().rstrip())
for i in range(N):
    word = list(input().rstrip())
    result = []
    for j in range(0,len(word)):
        if j > 0 and word[j] == word[j-1]:
            continue
        else:
            result.append(word[j])
    max_alp = list(Counter(result).most_common())[0][1]
    if max_alp == 1:
        count += 1

print(count)
#########################
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find): # sorted http://blog.weirdx.io/post/50236 , find 처음 문자 순서대로 sorted 되는듯
        result += 1
print(result)
