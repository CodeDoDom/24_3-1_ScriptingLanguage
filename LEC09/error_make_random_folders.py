import os
import random

folder_no = 0

def make_random_folders(count):
    global folder_no

    if not count: return

    os.mkdir(f'folder{folder_no}')
    os.chdir(f'folder{folder_no}')

    folder_no += 1
    count -= 1
    while count:
        subcount = random.randint(0, count)
        make_random_folders(subcount)
        count -= subcount


report_home = 'C:/TestFolder'


def make_random_root_folder():
    assert not os.path.exists('root_folder'), "root folder already exists!"
    os.mkdir('root_folder')
    os.chdir('root_folder')
    make_random_folders(10)
    os.chdir('..')

os.chdir(report_home)
make_random_root_folder()






