import sys
input = sys.stdin.readline

num = 123456 * 2 + 1
prime = [False] * num

for i in range(1, num):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5)+1 ):
        if i%j==0:
            break
    else:
        prime[i-1] = True

N = None
while N !=0 :
    N = int(input().rstrip())
    count = 0
    for i in range(N+1, 2*N+1):
        if prime[i-1] :
            count += 1
    print(count)
