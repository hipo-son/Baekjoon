import sys
input = sys.stdin.readline
T = int(input().rstrip())

num = 10000 + 1
prime = [False] * num

for i in range(1, num):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5)+1 ):
        if i%j==0:
            break
    else:
        prime[i-1] = True

for i in range(T):
    N = int(input().rstrip())
    list = [False] * N
    for j in range(1, N+1):
        if prime[j-1] :
            list[j-1] = True
    for k in range(int(N/2), N + 1):
        if list[k-1] and list[(N - k)-1] :
            print((N - k) , k)
            break
