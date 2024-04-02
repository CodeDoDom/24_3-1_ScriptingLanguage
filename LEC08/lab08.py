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
