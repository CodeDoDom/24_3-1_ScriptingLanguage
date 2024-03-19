a_student = {'name':'Hana', 'grade':'B'}
type(a_student)
a_student['name']
a_student['grade']
a_student['age'] = 20
a_student

data = {'color':'red', 'age':'42'}

'color' in data     #True   in은 key에 대해서만 작동함
'red' in data       #False  data.values()로 쓰면 True

for k in data.keys():
    print(k)
for v in data.values():
    print(v)
for k, v in data.items():
    print(f'{k=}, {v=}')

a_student['gender']
a_student.get('gender')     # a_student['gender']보다 안정적임
a_student.get('height', 176)

# setdefault()
spam = {'name':'Pooka', 'age':5}
spam.setdefault('color', 'black')
spam
spam.setdefault('color', 'white')
spam

# characterCounter.py v.1
text = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for c in text:
    count.setdefault(c, 0)
    count[c] += 1
print(count)

# characterCounter.py v.2
text = 'It was a bright cold day in April, and the clocks were striking thirteen.'
from collections import defaultdict

count = defaultdict(lambda: 0)
for c in text:
    count[c] += 1

print(count)
print(type(count))

# set
s = {1, 2, 3}
type(s)     # set
t = {3, 4, 5}
s|t     # 합집합
s&t     # 교집합
s - t   # 차집합
t - s

s.add(8)
s

{1,2} == {2, 1}
