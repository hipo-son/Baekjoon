import sys
input = sys.stdin.readline
N = int(input().rstrip())

def primenumber(x):
    for i in range(2, x):
    	if x % i == 0:
        	return False
    return True

def findPrimes(n):
      primes = []
      for i in range(2, (n//2)+1):
          if primenumber(i):
              primes.append(i)
      return primes

def factorize(n):
      factors = []
      primes = findPrimes(n)
      for i in primes:
          while (n % i == 0):
              factors.append(i)
              n = n // i
      return factors

for i in factorize(N):
    print(i)
################################################ fix
import sys
input = sys.stdin.readline
N = int(input().rstrip())

N = int(input())

for i in range(2, N+1):
    a = 0
    if a == 0:
        while N % i == 0:
            print(i)
            N //= i
    if N - i == 0:
        break
