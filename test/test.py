def sum_underfloor(x):
    result = 0
    for j in range(0, x +1):
        result += n_n[j]
    return result

n_n = [i for i in range(1, 15)]
for k in range(1,3):
    n_n = list(map(sum_underfloor, range(0,14)))
    print(n_n)

print(n_n[])
