num = [i for i in range(1, 10)]

def rows(x) :
    tmp = set(num)
    for i in range(9) :
        tmp -= set([Li[x][i]])
    if len(tmp) != 0 :
        return list(tmp)
    else:
        return []


Li = [[0,2,3,4,5,6,7,8,9],[],[],[],[],[],[],[],[]]

print(rows(0))
