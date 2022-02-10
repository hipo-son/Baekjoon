num = input().split()
A, B = int(num[0]), int(num[1])

if A > B :
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')
