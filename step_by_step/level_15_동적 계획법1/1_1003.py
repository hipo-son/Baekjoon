import sys
input = sys.stdin.readline

def fibo_index(x):
    if x in Li:
        return Li[x]
    else:
        a = fibo_index(x-1)[0] +  fibo_index(x-2)[0] # 0
        b = fibo_index(x-1)[1] +  fibo_index(x-2)[1] # 1
        Li[x] = [a, b]
        return Li[x]

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    Li = {0: [1, 0], 1:[0, 1]}
    f = fibo_index(N)
    print(f[0],f[1])
    # print(Li)
