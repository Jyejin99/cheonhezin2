from urllib import response
# <BeautifulSoup 모듈>
# BeutifulSoup 네이버 뉴스 언론사 가져오기
'''
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com")
html = req.text
soup = BeautifulSoup(html, 'html.parser')

result = soup.find_all('a','thumb')
news_list = []
for i in result:
    news_list.append(i.find("img")["alt"])
print(news_list)
'''
'''
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com")
html = req.text
soup = BeautifulSoup(html, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.img)
print(soup.img['alt'])
#print(soup.img['class'])
print(soup.img['height'])

print(soup.find('a'))
print(soup.find(id='search'))
'''
# find_all - HTML 해당 태그에 대한 모든 정보를 리스트 형식으로 가져옴
'''
print(soup.find_all('a',limit=2))
#limit - 개수 지정
print(soup.find_all('a')[0])
print(soup.find_all('span',class_="blind"))
print(soup.find_all('span',attrs={"class":"blind"}))
'''
# string으로 검색 - 해당 값이 있는지 없는지 검사 할 때 활용
'''
print(soup.find_all(string='자동완성 끄기'))

import re
print(soup.find_all(string=re.compile("네이버")))
'''
# select() - CSS 선택자를 활용하여 원하는 정보를 가져옴
'''
print(soup.select_one('a'))
print(soup.select("body a"))
print(soup.select('div > ul'))
'''
# get_text() - 검색 결과에서 태그를 제외한 텍스트만 출력
'''
text = soup.find("span", attrs={"class":"blind"})
print(text)
print(text.get_text())
print(text.get('class'))
print(text.string)
'''
# 영화 인기 순위 출력하기
'''
import requests
from bs4 import BeautifulSoup
req = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
movie_ranking_list = soup.find_all('div',class_="tit3")
for i in range(len(movie_ranking_list)):
    print("{:2} 위 : {}".format(i+1,movie_ranking_list[i].get_text().strip()))
'''
# 실시간 인기 뉴스 출력하기

import requests
from bs4 import BeautifulSoup
import re

req = requests.get('https://media.naver.com/press/082')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
news_list = soup.find_all('span',class_="press_edit_news_title")
for i in range(10):
    print("{:2} 번 : {}".format(i+1,news_list[i].get_text().strip()))


