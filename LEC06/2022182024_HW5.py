import keyboard
import pyperclip


def copy_clipboard_to_sen():    # 클립보드에 저장된 내용을 sen에 저장함
    global sen
    sen = pyperclip.paste()
    split_sentence(sen)
    count_words(words)
    print_cnt_words(cnt_word, 20, 20)


def split_sentence(sen):   # 문자열 sen을 공백 기준으로 분리
    global words
    print(f'원본 문장: {sen}')
    words = sen.split()


def count_words(words):
    global cnt_word
    cnt_word = {}
    for word in words:
        if word.isalpha():  # 단어가 알파벳으로만 이루어져있다면
            cnt_word[word] = cnt_word.get(word, 0) + 1
    return cnt_word


def print_cnt_words(cnt_word, lwidth, rwidth):
    print('Word Count'.center(lwidth + rwidth, '='))
    for k, v in cnt_word.items():
        print(k.ljust(lwidth, ' ') + str(v).rjust(rwidth))


keyboard.add_hotkey('shift+windows+w', copy_clipboard_to_sen)
keyboard.wait('esc')
keyboard.remove_all_hotkeys()
