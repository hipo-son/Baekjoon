N = int(input())
count = 0
for num in range(N , 0, -1):
    if num < 10:
        count += 1
    elif num < 100:
        tmp = list(map(int, str(num)))
        for i in range(-9, 10):
            if tmp[0] + i == tmp[1]:
                count += 1
    elif num < 1000:
        tmp = list(map(int, str(num)))
        for i in range(-9, 10):
            if tmp[0] + i == tmp[1] and tmp[1] + i == tmp[2]:
                count += 1
print(count)
