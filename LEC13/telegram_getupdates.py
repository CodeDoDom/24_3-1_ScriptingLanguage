import requests
import json

telegram_url = 'https://api.telegram.org/bot6798029428:AAFBkl4jML2eqm6UGz5QO1bOOkp9a2JT5b4'


def show_update(u):
    if 'message' in u:  # 업데이트가 메시지라면,
        msg = u['message']
        sender_username = msg['from'].get('username', 'NOUSERNAME')
        sender_fullname = msg['from'].get('first_name', '') + ' ' + msg['from'].get('last_name', '')
        if 'text' in msg:   # 메시지가 텍스트로 있으면, 파일만 보내는 경우도 있으므로
            text = msg['text']
            print(f'{sender_fullname}({sender_username}) : {text}')
        else:
            print(json.dumps(msg, indent=2, ensure_ascii=False))


with open('status.json') as f:
    status = json.load(f)

r = requests.get(f'{telegram_url}/getUpdates', params={'offset': status['last_update_id'] + 1})
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
