A , B = 1, 2

distance = 1
count, total, tmp = 0, 0, 0
i = 1
while distance > total:
    if tmp == 1:
        tmp = 0
        total += i
        i += 1
    else:
        tmp += 1
        total += i
    count += 1
print(count)
