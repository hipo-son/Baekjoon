import sys
input = sys.stdin.readline

N = 5 * 2 + 1
sieve = [False] * N   # 중요
for i in range(2, N * 2 + 1):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5)+1):
        if i%j==0:
            break
    else:
        sieve[i] = True

print(sieve)

while N !=0 :
    N = int(input().rstrip())
    count = 0
    for i in range(N+1, 2*N+1):
        if i in prime:
            count += 1
    print(count)
