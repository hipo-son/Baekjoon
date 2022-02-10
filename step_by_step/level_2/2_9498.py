exam_score = int(input())

if 100 >= exam_score >= 90:
    print('A')
elif 90 > exam_score >= 80:
    print('B')
elif 80 > exam_score >= 70:
    print('C')
elif 70 > exam_score >= 60:
    print('D')
else:
    print('F')
