import random

students = []       # 리스트

kor_total = 0
eng_total = 0
math_total = 0

for _ in range(20):
    kor_grades = random.randint(0, 100)
    eng_grades = random.randint(0, 100)
    math_grades = random.randint(0, 100)
    student_avg = (kor_grades + eng_grades + math_grades) / 3   # 학생 평균

    kor_total += kor_grades
    eng_total += eng_grades
    math_total += math_grades

    student = {'KOR': kor_grades, 'ENG': eng_grades, 'MATH': math_grades, 'AVG': student_avg}   # 딕셔너리
    students.append(student)

kor_avg = kor_total / 20
eng_avg = eng_total / 20
math_avg = math_total / 20

print('=======================================')
print('NUM\t\tKOR\t\tENG\t\tMATH\tAVG')
print('---------------------------------------')

for i in range(20):
    print("{num}\t\t{KOR}\t\t{ENG}\t\t{MATH}\t\t{AVG}".format(num=i + 1, KOR=students[i]['KOR'],
                                                              ENG=students[i]['ENG'], MATH=students[i]['MATH'],
                                                              AVG=round(students[i]['AVG'], 2)))

print('---------------------------------------')
print(f'AVG\t\t{kor_avg}\t{eng_avg}\t{math_avg}')
print('=======================================')
