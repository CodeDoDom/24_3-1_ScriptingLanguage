import requests
import json
import uuid
import os

telegram_url = 'https://api.telegram.org/bot7011406171:AAHEiA90Nk0HGri4IoLYp6St0OHo5PiPnyc'
telegram_file_url = 'https://api.telegram.org/file/bot7011406171:AAHEiA90Nk0HGri4IoLYp6St0OHo5PiPnyc'


def download_file(doc):
    file_name = doc['file_name']
    file_id = doc['file_id']

    # 실제 파일 위치를 가져온다.
    r = requests.get(f'{telegram_url}/getFile', params={'file_id': file_id})
    if r.ok:
        server_file_path = r.json()['result']['file_path']
        print(f'downloading... {file_name} at {server_file_path}')
        r = requests.get(f'{telegram_file_url}/' + server_file_path)
        if r.ok:
            with open(file_name, 'wb') as wf:
                wf.write(r.content)
        else:
            print(f'FAIL: {r.json()}')
    else:
        print(f'FAIL: {r.json()}')


# 실행 안됨
def download_photo(photo):
    file_id = photo[-1]['file_id']

    # 실제 파일 위치를 가져온다.
    r = requests.get(f'{telegram_url}/getFile', params={'file_id': file_id})
    if r.ok:
        server_file_path = r.json()['result']['file_path']
        file_name = f'myimg{uuid.uuid4().int}' + os.path.splitext(server_file_path)[-1]
        print(f'downloading... {file_name} at {server_file_path}')
        r = requests.get(f'{telegram_file_url}/' + server_file_path)
        if r.ok:
            with open(file_name, 'wb') as wf:
                wf.write(r.content)
        else:
            print(f'FAIL: {r.json()}')
    else:
        print(f'FAIL: {r.json()}')


def show_update(u):
    if 'message' in u:  # 업데이트가 메시지라면,
        msg = u['message']
        chat_id = msg['chat']['id']
        sender_username = msg['from'].get('username', 'NOUSERNAME')
        sender_fullname = msg['from'].get('first_name', '') + ' ' + msg['from'].get('last_name', '')
        if 'text' in msg:   # 메시지가 텍스트로 있으면, 파일만 보내는 경우도 있으므로
            text = msg['text']
            print(f'[{chat_id}] {sender_fullname}({sender_username}) : {text}')
        elif 'document' in msg:
            download_file(msg['document'])
        elif 'photo' in msg:
            download_photo(msg['photo'])
        else:
            print(json.dumps(msg, indent=2, ensure_ascii=False))


with open('status.json') as f:
    status = json.load(f)

r = requests.get(f'{telegram_url}/getUpdates',
                 params={'offset': status['last_update_id'] + 0})
if r.ok:
    assert r.headers['content-type'] == 'application/json'

    updates = r.json()['result']    # list of updates
    if updates:
        for u in updates:
            show_update(u)
        status['last_update_id'] = updates[-1]['update_id']
        with open('status.json', 'w') as f:
            json.dump(status, f)

else:
    print(f'FAIL: {r.status_code}')
