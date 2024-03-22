# Raw String
print(r'That is Carol\'s cat.')


# Multiple Lines
def print_lines():
    print('''
애국가
    동해물과 백두산이 ....
    우리나라 만세 ....
끝.
''')


print_lines()

# Slicing
msg = 'hello, world!'
even_msg = msg[::2]
even_msg

# 문자열 포함 여부
'Hello' in 'Hello World'    # TRUE
'HELLO' in 'Hello World'    # FALSE
'' in 'hello'               # TRUE

# isX
'hello'.isalpha()       # 알파벳인가
'hello123'.isalpha()
'hello123'.isalnum()    #알파벳 또는 숫자인가
'hello'.isalnum()
'123'.isdecimal()       # 십진수인가
'  '.isspace()          # ?
'\r\t\n'.isspace()
'This Is Title Case'.istitle()  # 첫 번째 문자가 대문자인가

# upper, lower, isupper, islower

# startswith, endswith
# 뭘로 시작하고, 끝나는가

# join
':'.join(['cat', 'rat', 'bat'])
''.join(['cat', 'rat', 'bat'])
''.join([str(i) for i in range(20)])    # List Comprehension

# split
'my name is hana'.split()
'my name is hana\nHello world'.split()
'my name is hana'.split('is')

# 줄 단위로 분리

# partition

# center, rjust, ljust
'hello'.rjust(10)
'hello'.ljust(10)
'hello'.rjust(20, '*')
'hello'.center(10, '=')

def print_picnic(food, lwidth, rwidth):
    print('PICNINC FOOD'.center((lwidth + rwidth), '='))
    for k, v in food.items():
        print(k.ljust(lwidth,'.') + str(v).rjust(rwidth))


food = {'sandwiches':4, 'apples':12,'cups':4}
print_picnic(food, 12, 5)
print_picnic(food, 20, 6)

# strip, rstrip, lstrip
spam = '  hello   world   '
spam.strip()
spam.lstrip()
spam.rstrip()

# ord(), chr()

# clipboard text - pyperclip 모듈 사용
import pyperclip
pyperclip.copy('Hello form Python')
pyperclip.paste()
