import requests
import json

telegram_url = 'https://api.telegram.org/bot7011406171:AAHEiA90Nk0HGri4IoLYp6St0OHo5PiPnyc'


def send_message(chat_id, text):
    r = requests.get(f'{telegram_url}/sendMessage', params={'chat_id': chat_id, 'text': text})
    if r.ok:
        print(json.dumps(r.json()['result'], indent=2, ensure_ascii=False))
    else:
        print(f'FAIL : {r.json()}')


def send_photo(chat_id, link):
    r = requests.get(f'{telegram_url}/sendPhoto',
                     params={'chat_id': chat_id,
                             'photo': link})
    if r.ok:
        print(json.dumps(r.json()['result'], indent=2, ensure_ascii=False))
    else:
        print(f'FAIL: {r.json()}')


def send_document(chat_id, fname):
    with open(fname, 'rb') as f:
        files = {'document': f}
        r = requests.post(f'{telegram_url}/sendDocument', params={'chat_id': chat_id}, files=files)

    if r.ok:
        print(json.dumps(r.json()['result'], indent=4, ensure_ascii=False))
    else:
        print(f'FAIL: {r.json()}')


# send_message(-4246362640, "안녕하세요. 저는 윤이하나 봇입니다.")
# send_photo(-4246362640, "https://ssl.nexon.com/s2/game/maplestory/renewal/common/logo.png")
send_document(7020745084, 'SANABI.jpg')