# List
import copy

[1, 2, 3]
['cat', 'bat', 'rat', 'elephant']
['hello', 3.1415, True, None, 42]

black_pink = ['jisu', 'jeni', 'rose', 'risa']
black_pink[0]
#black_pink[4]
black_pink[-1]

# Slice
num = '0123456789ABCDEF'
num[0:5]
num[1:9:2]
num[::]
num[::2]
num[::-1]

black_pink[::-1]

# 변경, 삽입, 삭제
black_pink = ['jisu', 'jeni', 'rose', 'risa']
len(black_pink)
black_pink[0] = 'PYTHON'
black_pink.append('JYP')
black_pink += ['YG']  # 리스트와 리스트를 다함

twice = ['momo', 'sana', 'zwi']
unite = black_pink + twice
unite.remove('PYTHON')
del unite[-1]
unite.insert(2, 'IU')   # 0이면 맨 앞에 삽입됨

# 리스트 멤버 interation
black_pink = ['jisu', 'jeni', 'rose', 'risa']
# 오류남
#for member in black_pink:
#    print(member)

#for i, member in enumerate(black_pink):
#    print(f'{i+1}번 멤버는 {member}이다.')

# 리스트 멤버 여부 판별
'risa' in black_pink
'rose' not in black_pink
'PYTHON' not in black_pink

# 인덱스
black_pink.index('rose')
black_pink.index('hana')

# sort
data = [2, 5, 3.14, 1, -7]
data.sort()
data.sort(reverse=True)
data.append('cat')
data.sort()

data2 = ['top', 'four', 'start', 'a']
data2.sort()    # 문자열 간의 대소비교 가능: 아스키코드로 대소비교 함.
data2.sort(key=lambda x:len(x))      # 문자열의 길이로 비교

# 퀴즈    ?
data3 = [1, 3, 3.14, 2, 4, 'cat']
data3.sort(key=lambda x: x if type(x) in [int, float] else -999999999999999)
#data3.sort(key=lambda x: x if type(x) in [int, float] else -999999999999999*len(x))

# copy
data4 = [['jisu', 'rose'], [23, 24]]
# shallow copy 얕은 복사
data5 = data4   #same id
data5 = data4.copy()
data5[0][1] = 'jeni'
id(data4[0])
id(data5[0])
# deep copy 깊은 복사
data6 = [['jisu', 'rose'], [23, 24]]
data7 = data6   #same id
data7 = copy.deepcopy(data6)
data7[0][1] = 'jeni'
id(data6[0])
id(data7[0])

# List Comprehension
values = [i for i in range(10)]
values = [i for i in range(10) if i % 2 == 1]
# [1,2,3] ['a','b','c',]
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b', 'c']]
# flatten 기능
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattend = [n for v in vec for n in v]
