import keyboard
import pyperclip


def copy_clipboard_to_sen():    # 클립보드에 저장된 내용을 sen에 저장함
    global sen
    sen = pyperclip.paste()
    # keyboard.write(sen)
    split_sentence(sen)
    count_words(words)


def split_sentence(sen):   # 문자열 sen을 공백 기준으로 분리
    global words
    print(f'원본 문장: {sen}')
    words = sen.split()
    print(f'분리: {words}')


def count_words(words):
    pass


keyboard.add_hotkey('shift+windows+w', copy_clipboard_to_sen)
keyboard.wait('esc')
keyboard.remove_all_hotkeys()
