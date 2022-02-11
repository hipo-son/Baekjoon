def d(n): #함수 d
    n_list = list(map(int, list(str(n))))
    return n + sum(n_list)

result = []
total_list = set([])

for i in range(1, 10000):
    a_list = []
    num = i
    while num <= 10000:
        a_list.append(num)
        num = d(num)
    a_list = set(a_list[1:])
    total_list = total_list | a_list

result = set([x for x in range(1,10001)])
result = list(map(int, list(result - total_list)))

for i in sorted(result):
    print(i)
