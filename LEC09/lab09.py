# Raise Exception
'''
raise Exception

raise Exception('Door is not open')

raise ValueError

age0 = 15

raise ValueError(f'Too Young: {age0=}')
'''

# Exception Handling, Exception raise 이용, Traceback의 이용, 파일 저장
import traceback


def f3():
    age = int(input('Enter Age:'))
    if age < 18:
        print('you cannot enter.')


def f2():
    f3()


def f1():
    for i in range(5):
        try:
            f2()
        except Exception as err:
            traceback.format_exc()
            with open('error.log', 'a') as ef:
                ef.write(traceback.format_exc())

f1()

# Assertion - 로직에 대한 중간 점검
data = 100

assert data == 100

assert data < 100

