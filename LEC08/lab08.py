# 파일 생성 및 쓰기, 추가
import os
os.chdir(r'C:\2022182024\24_3-1_ScriptingLanguage\LEC08\TESTFOLDER')
os.getcwd()

f = open('sample.txt', 'w')
f.write('Hello, New World.')
f.close()

    # 뒤에 이어붙이기
with open('sample.txt', 'a', newline='\n') as f:
    f.write('This is Python.\n')
    f.write('I love Python.T_T\n')
    pass

# 파일 읽기
with open('sample.txt', 'r') as f:
    data = f.read()     # 몽땅 다 읽음
    print(type(data))
    print(data)

with open('sample.txt') as f:
    l = f.readline(); print(l, end='')  # 한 줄씩 읽음
    l = f.readline(); print(l, end='')

with open('sample.txt') as f:   # 모든 줄을 다 읽어들이려면
    for l in f:
        print(l, end='')

# 임의의 위치에 내용 추가
with open('sample.txt') as f:
    lines = f.readlines()

print(lines)

with open('sample.txt', 'w') as f:
    lines.insert(0, "Header".center(20, '=')+'\n')
    lines.append("Footer".center(20, '=')+'\n')
    f.writelines(lines)

# 이전 데이터 read & write
with open('binary.dat', 'wb') as f:
    f.write(b'0123456789abcdefg')

with open('binary.dat', 'rb') as f:
    f.read(1)   # 첫 번째 한 바이트 읽기
    f.read(1)

f = open('binary.dat', 'rb')
f.read(1)

# 파일 정보
os.chdir('C:/Windows/System32')
os.getcwd()
os.listdir()
os.path.getsize('calc.exe')
creation_time = os.path.getctime('calc.exe')
modified_time = os.path.getmtime('calc.exe')
a_time = os.path.getatime('calc.exe')

import time
time.ctime(creation_time)
time.ctime(modified_time)
time.ctime(a_time)

# Dir Name, Base Name
path = r'c:\2022182024\24_3-1_ScriptingLanguage\test.py'
os.path.basename(path)
os.path.dirname(path)
os.path.split(path)
os.path.splitext(path)

# Working Dirctory(folder)
import os
os.chdir(r'C:\2022182024\24_3-1_ScriptingLanguage\LEC08\TESTFOLDER')
os.getcwd()

os.mkdir('temp')
os.makedirs(r'test\test')

os.chdir(r'c:/')
os.makedirs('newFolder')

# 0405(금)
# 폴더 전체 구조 탐사 os.walk()
import os
os.chdir(r'C:\TESTFOLDER')
for root, subfolders, files in os.walk(r'.\Python312'):
    print('info'.center(40, '='))
    print(f'{root}')
    print(f'{subfolders}')
    print(f'{files}')

# 파일과 폴더 복사와 이동
import shutil
shutil.copy('NEWS.txt', 'NEWS2.txt')
shutil.copytree('Doc', 'Doc2')
shutil.move('python3.dll', 'python4.dll')
shutil.move('Doc2', 'Doc3')

# 파일과 폴더 삭제
os.unlink('NEWS2.txt')
os.remove('NEWS.txt')
os.rmdir('tcl')
shutil.rmtree('tcl')

# 휴지통 보내기 - send2trash 모듈 이용
import send2trash
import os

os.chdir(r'C:\TESTFOLDER\Python312')    # 워킹 디렉토리 설정
send2trash.send2trash('python.exe')

# 휴지통 보내기 - winshell 모듈 이용
# 휴지통에서 다시 복구할 수 있음
import winshell

winshell.delete_file('python4.dll')

    # 간단한 복구
for item in winshell.recycle_bin():
    item.undelete()

winshell.delete_file('pythonw.exe')
winshell.delete_file('python312.dll')

# 휴지통 내용 확인
for item in winshell.recycle_bin():
    print(item.real_filename(), item.original_filename(), item.attributes())

# zip 파일 읽기
import zipfile

zf = zipfile.ZipFile('include_test.zip')
zf.namelist()
zf.getinfo('include/abstract.h')
zf.extract('include/abstract.h')    # 특정 파일 압축 풀기

# zip 파일 만들기
zf = zipfile.ZipFile('new.Zip', 'w')
zf.write('Python4.dll', compress_type=zipfile.ZIP_DEFLATED)
zf.close()

zf = zipfile.ZipFile('new.Zip', 'a')
zf.write('pythonw')
zf.close()

# sort
import random

a = {random.randint(1, 1000): 'TEST' for _ in range(10)}
a
sorted(a)

data = {'jisu':170, 'momo':160, 'iu':175}
sorted(data)
data.items()
sorted(data.items(), key=lambda x: x[1])    # 오름차순
sorted(data.items(), key=lambda x: x[1], reverse=True)  # 내림차순
