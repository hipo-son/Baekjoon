import sys
input = sys.stdin.readline
M, N = map(int, input().rstrip().split())

n = N
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(1,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

for num in range(M, N, 2):
    if num in primes:
        print(num)
