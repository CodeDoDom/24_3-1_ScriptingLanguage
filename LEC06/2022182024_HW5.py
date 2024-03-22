import keyboard
import pyperclip


def split_sentence(sen):   # 문자열 str을 공백 기준으로 분리
    print(f'{sen}')


def copy_clipboard_to_sen():    # 클립보드에 저장된 내용을 str에 저장함
    global sen
    sen = pyperclip.paste()
    # keyboard.write(sen)
    split_sentence(sen)


keyboard.add_hotkey('shift+windows+w', copy_clipboard_to_sen)
keyboard.wait('esc')
keyboard.remove_all_hotkeys()
