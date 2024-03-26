import re

# 기본 사용 - 문자열 검색
p = re.compile('Hello')
text = 'Hello, world and world.'
p.search(text)
p = re.compile('World')

# 그룹화 괄호 사용
import re
text = '1234-5678'
p = re.compile(r'(\d{4})-(\d{4})')      # 괄호로 감싸진 부분이 group
mo = p.search(text)                     # matching objects
station_no, user_no = mo.groups()
station_no
user_no

p = re.compile(r'([a-zA-Z]+)(at)')
p.findall(test_string)

# .* 모든 문자열에 매칭
text = '성: 이    이름: 대현'
p = re.compile('성:([ ]*.*)이름:(.*)')
mo = p.search(text)
mo.groups()