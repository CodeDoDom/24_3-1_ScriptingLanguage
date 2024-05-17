import requests
import json

YOUR_CLIENT_ID = ''
YOUR_CLIENT_SECRET = ''

# 네이버 쇼핑 API URL
url = "https://openapi.naver.com/v1/search/shop.json"

# API 요청 헤더
headers = {
    "X-Naver-Client-Id": YOUR_CLIENT_ID,
    "X-Naver-Client-Secret": YOUR_CLIENT_SECRET
}

# API 요청 파라미터
params = {
    "query": "신라면",
    "display": 20,
    "sort": "asc"
}

# API 요청
response = requests.get(url, headers=headers, params=params)

# 응답 데이터 파싱
data = json.loads(response.text)

# 상품 정보 출력
for item in data['items']:
    print(f"상품명: {item['title']}, 최저가: {item['lprice']}원")
