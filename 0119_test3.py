#3번 : 네이버 뉴스 기사 가져오기

import requests

f = open("test.html",'w',encoding='UTF-8')
URL = 'https://news.naver.com'
response = requests.get(URL)
print(response.text)
html_source = response.text
f.write(html_source)
f.close()