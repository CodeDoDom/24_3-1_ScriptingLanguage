import re

# 지역 번호 또는 010 체크
# 지역 번호에 괄호가 없는 경우
p = re.compile(r'''
    010|02|051|053|032|062|042|052|044|031|033|043|041|063|061|054|055|064      # 010 또는 지역 번호, 괄호가 없는 경우
''', re.VERBOSE)

# 010 또는 지역 번호, 괄호가 있는 경우
p = re.compile(r'''
    \(                  # 괄호 자체
    010|02|051|053|032|062|042|052|044|031|033|043|041|063|061|054|055|064
    \)                  #닫는 괄호
''', re.VERBOSE)

# 010 또는 지역 번호 (괄호가 있어도 되고, 없어도 됨)
p = re.compile(r'''
    ^
    (                                                                                       # group1
        (                                                                                   # group2
            (010|02|051|053|032|062|042|052|044|031|033|043|041|063|061|054|055|064)        # group3   # 010 또는 지역 번호, 괄호가 없는 경우
            |
            \(                                                                              
                (010|02|051|053|032|062|042|052|044|031|033|043|041|063|061|054|055|064)    # group4
            \)                                                                              
        )
        [ ]*-?[ ]*                          # 중간 대시, 공백, 또는 아예 없거나
    )?
    ([123456789]\d{2,3})                  # 국번: 0이 아닌 숫자로 시작, 3자리 또는 4자리            # group5
    [ ]*-?[ ]*                          # 중간 대시, 공백, 또는 아예 없거나
    (\d{4})                               # 개별 번호: 4자리                                      # group6
    $
''', re.VERBOSE)

p = re.compile(r'''
    ^
    (                                                                                       
        (                                                                                   
            (010|02|051|053|032|062|042|052|044|031|033|043|041|063|061|054|055|064)         
            |
            \(                                                                              
                (010|02|051|053|032|062|042|052|044|031|033|043|041|063|061|054|055|064)    
            \)                                                                              
        )
        [ ]*-?[ ]*                          
    )?
    ([123456789]\d{2,3})                  
    [ ]*-?[ ]*                        
    (\d{4})                             
    $
''', re.VERBOSE)

# 지역번호국번개별번호
# 공백 또는 대시, 또는 아예 없는 경우
p = re.compile(r'''
    [ ]*-?[ ]*                          # 중간 대시, 공백, 또는 아예 없거나
''', re.VERBOSE)

p = re.compile(r'''
    [123456789]\d{2,3}                  # 0이 아닌 숫자로 시작, 3자리 또는 4자리
''', re.VERBOSE)

# 개별 번호
p = re.compile(r'''
    \d{4}      # 4자리
''', re.VERBOSE)


# 테스트 코드

p.search('010')
p.search('02')
p.search('111')

# 정상적인 번호 리스트 작성
good_numbers = [
    '(031) 8041 - 0550', '3533435', '34239872', '353 3435', '01034243424',
    '(031) - 8041 0123', '(010) - 333 - 4444'
]

# 잘못된 번호 리스트 작성
bad_numbers = [
    '010333344444', '010 - 3333 - 444', '099 - 353 - 3435', '010 - 34 - 34554', '342498765'
]


def test_good_cases():  # 정상적인 번호에 대해 테스트하는 코드
    for s in good_numbers:
        mo = p.search(s)
        if not mo:
            print(f'Failed for good number {s}')
        else:
            print(s, '--> ', end='')
            if mo.group(3):     # 괄호없는 지역번호, 핸폰번호 존재
                print(f'({mo.group(3)}) - {mo.group(5)} - {mo.group(6)}')
            elif mo.group(4):   # 괄호있는 지역번호, 핸폰번호 존재
                print(f'({mo.group(4)}) - {mo.group(5)} - {mo.group(6)}')
            else:               # 핸폰번호로 간주
                print(f'(010) - {mo.group(5)} - {mo.group(6)}')


def test_bad_cases():   # 비정상적인 번호에 대해 테스트하는 코드
    for s in bad_numbers:
        mo = p.search(s)
        if mo:
            print(f'Failed for bad number {s} : {mo.group()}')
        else:
            print(f'{s} --> Wrong Number')


def test_all():
    test_good_cases()
    test_bad_cases()


test_all()


import exrex

for i in range(100):
    # exrex.getone(): 특정 패턴을 갖는 문자열을 랜덤으로 생성  # *: 없거나 여러개 있거나
    print(exrex.getone(r'\d*', 5))

p.pattern   # 원래 정규식의 문자열이 그대로 들어있다.
pattern_str = re.sub(r'[ ]{2,}|\t|\n', '', p.pattern)   # 2개 이상의 연속된 공백과 개행 문자 삭제

for i in range(10):
    print(exrex.getone(pattern_str, 2))
