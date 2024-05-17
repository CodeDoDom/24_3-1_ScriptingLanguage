from playwright.sync_api import sync_playwright
import time
import bs4
import requests
from bs4 import BeautifulSoup

word = '신라면'
url = f'https://search.shopping.naver.com/search/all?origQuery={word}&pagingIndex=1&pagingSize=40&productSet=total&query={word}&sort=price_asc&timestamp=&viewType=list'

# not working 2024
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
# }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

p = sync_playwright().start()
browser = p.chromium.launch(headless=False).new_context(
    user_agent=headers['User-Agent'], viewport={'width':800, 'height':600}
)

page = browser.new_page()
page.goto(url)

# page.keyboard.press('End')

src_size = 0
while src_size < len(page.content()):
    src_size = len(page.content())
    page.keyboard.press('End')
    time.sleep(1)



# r = requests.get(url, headers=headers)
# r.raise_for_status()
#
# with open('download.html', 'w', encoding='utf-8') as wf:
#     wf.write(r.text)

# 제품명
# <a target="_blank" rel="noopener" class="product_link__TrAac linkAnchor" title="농심 신라면블랙 134g 4개입 멀티팩 간편한" data-nclick="N=a:lst*N.title,i:46539817522,r:1" data-i="46539817522" data-ms="24" href="https://cr.shopping.naver.com/adcr.nhn?x=bPNLPV6cerA5%2BBHNZpBeev%2F%2F%2Fw%3D%3DsD9fgJesQTThz9PLAx0HPXtOWpglJD7olF9kCPPNKTJ2wBi3LAWoXSDALXUpoZu8tV22oypXajZUF7Ds9q3J2kNNvW3C8hT5XJiSOS%2Fuam3ARIjT978VbcCz6yMKlZYwSHIM1r43vGM5LeQJPBw3yAZVPHTMZ%2FdayecNOlr81VlBQTyXfOvCSfTks0sOoDonCLM9wEkW%2B1N5NkY8B6AAqfQ3%2BGhXrKDk5o55fYdTwSvjvIw%2Fwmw1Akxc3Se6AA4jE5Kl2jVLXNdxHkJe3i8r%2B8CZXm%2F05hnH8uOMWFca5%2FzvhM25zJO1Gee756Kw1ZIXyZTHYHHjea2%2B%2Fct9dbVkIjIrHsbeStsmJBfOvK7DA6omK1brdg3%2FV%2F68j5aldrfVcF1hrSdShD3KQCRc14XkyqRzngVRtkmUiTOAHJ5K8D3u034svgJpXQx0Xl3XfBkuAWcpqAOGTUKDl2j9FOvYq8tFbj3LLuyieepuMB5dRe7msR3e%2F0gxHbWcieFjmxbDBclrQObt0Ew8iP7ntO5AVbkfVydCRgK1tighrqPuB%2F1OhI7DyFZ70IXufRpGHV1uaA7i8K8Up6jGkn8DwQgfH%2F3R9INs9ZpxiOekV5%2FkbMXFs19boglJ5g0tUGAN2KuK9W7NztEFs%2Bc9UgSk7XvVZhFdznR4EhPC6BI08fc6TT2xWkbDrUFJ2hBG8QaB8WVzn&amp;nvMid=46539817522&amp;catId=50013941">농심 신라면블랙 134g 4개입 멀티팩 간편한</a>
selector = '[class^="product_link"][title]'
soup = bs4.BeautifulSoup(page.content(), 'html.parser')
elms = soup.select(selector)
for e in elms:
    print(e['title'])

# 가격
# <span class="price"><span class="price_num__S2p_v"><em>10,000</em>원</span></span><span class="price"><span class="price_num__S2p_v"><em>10,000</em>원</span></span>
# selector: .price
elms = soup.select('.price')
for e in elms:
    print(e.get_text())

select = '[class^="product_item"]'

elms = soup.select(select)
for e in elms:
    title = e.select_one('[class^="product_link"][title]')['title']
    price = e.select_one('.price').text
    print(f'{title}: {price}')

browser.close()
p.stop()
