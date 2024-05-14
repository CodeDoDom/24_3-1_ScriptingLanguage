from bs4 import BeautifulSoup
import requests

keyword = '신라면'
url = f'https://www.google.com/search?q={keyword}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

r = requests.get(url, headers=headers)
r.raise_for_status()
# with open('download.html', 'w', encoding='utf-8') as wf:
#     wf.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
for i, e in enumerate(soup.select("#search a h3")):
    print(f'#{i} {e}')
