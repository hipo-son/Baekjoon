N = int(input())

Li = list(map(int, input().split()))

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for i in Li[1:]:
    tmp = gcd(Li[0], i)
    print('{0}/{1}'.format(int(Li[0]/tmp), int(i/tmp)))
