import sys
input = sys.stdin.readline

N = int(input().rstrip())
Li = []
for i in range(N): # [a, b] 형태로 저장
    a, b = map(int, input().rstrip().split())
    Li.append([a, b])

Li.sort(key = lambda a: a[0]) # 시작시간이 동일시 일때는 시작시간이 빨라야 한다 (조건 2)
Li.sort(key = lambda a: a[1]) # 회의의 종료시간이 빨라야 한다 (조건 1)

cnt , last = 0, 0
print(Li)
for i, j in Li:
    if i >= last:
        cnt += 1
        last = j

print(cnt)
