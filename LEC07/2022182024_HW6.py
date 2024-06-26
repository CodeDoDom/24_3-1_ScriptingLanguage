import re

test_phone_number = '''
(031) 8041 - 0550

3533435
34239872
353 3435
01034243424

(031) - 8041 0123
(010) - 333 - 4444

010333344444
010-3333-444
010 333 3444
3542 - 8795
099 - 353 - 3435
010 - 34 - 34554
342498765
'''
p = re.compile(
    r'((\(?((010)|(02)|(051)|(053)|(032)|(062)|(042)|(052)|(044)|(031)|(033)|(043)|(041)|(063)|(061)|(054)|(055)|(064))\)?)? ?-? ?\d{3,4} ?-? ?\d{4})')
# p = re.compile(r'''((\(?((010)|(02)|(051)|(053)|(032)|(062)|(042)|(052)|(044)|(031)|(033)|(043)|(041)|(063)|(061)|(054)|(055)|(064))\)?)?[ - ]?\d{3,4}[ - ]?\d{4})''')

print('[전화번호 검사 및 포맷터 구현 결과]')
print('------------------------------')

# 정규식과 일치하는 문자열 찾기
matches = p.findall(test_phone_number)

print('Collect Number:')
# 일치하는 문자열 출력
for match in matches:
    print(match[0])

# 출력 예시
'''
(031) 8041 - 0550 --> (031) 8041 - 0550

3533435 --> (010) 353 - 3435
34239872 --> (010) 3424 - 9872
353 3435 --> (010) 353 - 3435
01034243424 --> (010) 3424 - 3424

(031) - 8041 0123 --> (031) 8041 - 0123
(010) - 333 - 4444 --> (010) 333 4444

010333344444 --> Wrong Number
010-3333-444 --> Wrong Number
010 333 3444 --> (010) 333 - 3444
3542 - 8795 --> (010) 3542 - 8795
099 - 353 - 3435 --> Wrong Local Number
010 - 34 - 34554 --> Wrong Number
342498765 --> Wrong Number
'''