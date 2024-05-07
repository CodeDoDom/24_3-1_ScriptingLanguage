import requests
import json

telegram_url = 'https://api.telegram.org/bot6798029428:AAFBkl4jML2eqm6UGz5QO1bOOkp9a2JT5b4'

r = requests.get(f'{telegram_url}/getMe')
if r.ok:
    assert r.headers['content-type'] == 'application/json'
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
