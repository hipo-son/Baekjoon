x = int(input())
y = int(input())

if x > 0:
    if y > 0: #1사분면
        print('1')
    elif y < 0: #4사분면
        print('4')
if x < 0:
    if y > 0: #2사분면
        print('2')
    elif y < 0: #3사분면
        print('3')
