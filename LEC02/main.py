import sys

# id(a)
a = [1, 2, 3, 4]
# b = a   # a와 b는 같은 오브젝트를 가리키게 됨
b = a.copy()    # b에 a 값 대입
b.remove(1)
print(a)
print(b)
id(a)
id(b)

# is 와 ==
# is: 값은 객체인가? 주소 비교
# ==: 같은 값인가?
is_a = 1000
is_b = 1000
is_a == is_b
is_a is is_b
id(is_a)
id(is_b)

is_c = 'abcd'
is_d = 'abcd'
is_c == is_d
is_c is is_d    # 인터닝 되어 True로 나옴
id(is_c)
id(is_d)

is_x = 3
is_y = 3
id(is_x)
id(is_y)
is_x is is_y    # 인터닝 되어 True로 나옴

# Interning(인터닝)
# 자주 사용하는 상수들을 인터닝하여 동일한 id를 갖게 만듦
# 메모리를 최적화하기 위함
# 정수: -5 ~ 256, 문자열: 대소문자와 숫자로 구성된 문자열
intern_a = 'hello'
intern_b = 'hello'
intern_a is intern_b    # True

intern_a = 'hello, world'
intern_b = 'hello, world'
intern_a is intern_b    # False

intern_c = '파이썬'
intern_d = '파이썬'
intern_c is intern_d    # False

intern_c = 'PYTHON'
intern_d = 'PYTHON'
intern_c is intern_d    # True

# intern()
# 상수에 대해서 강제적으로 내부 캐싱을 통해 속도를 높임
intern_c = sys.intern('파이썬')
intern_d = sys.intern('파이썬')
intern_c is intern_d    #True

intern_e = 'Good'
intern_f = 'Bye'
intern_g = intern_e + intern_f  # 상수가 아니면 적용되지 않음
intern_h = intern_e + intern_f
intern_g is intern_h    # False
