# <urllib 모듈>
'''
import urllib

URL = 'https:///www.naver.com'
response_urllib = urllib.request.urlopen(URL)
byte_data = response_urllib.read()
text_data = byte_data.decode('utf-8')
print(text_data)
'''
'''
import urllib.request

URL = 'https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8'
request = urllib.request.Request(URL)
#print(request)
#print(request.full_url)
#print(request.type)
print(request.host)
'''
'''
import urllib.request

URL = 'https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8'
request = urllib.request.Request(URL)
response1 = urllib.request.urlopen(request)
response2 = urllib.request.urlopen(URL)
print(response1)
print(response2)
'''
'''
from urllib import response
import urllib.request

URL = 'https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8'
response_urllib = urllib.request.urlopen(URL)
byte_data = response_urllib.read(500)
print(byte_data)
'''

# byte 형식의 데이터를 원하는 형식으로 반환
'''
from urllib import response
import urllib.request

URL = 'https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8'
response_urllib = urllib.request.urlopen(URL)
byte_data = response_urllib.read(500)
text_data = byte_data.decode()
print(text_data)
'''
'''
import urllib.request

img_src = 'https://media.nationalgeographic.org/assets/photos/000/276/27633.jpg'
new_name = 'earth_img.jpg'
urllib.request.urlretrieve(img_src, new_name)
'''

# parse - url을 파싱하여 분석하기 위한 모듈
'''
import urllib.parse as ul

parse = ul.urlparse('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%9B%B9%ED%88%B0')
print(parse)
print(parse.query)
print(type(parse.query))

qs = ul.parse_qs(parse.query)
print(qs)
print(type(qs)) #딕셔너리 형태로 반환

qsl = ul.parse_qsl(parse.query)
print(qsl)
print(type(qsl)) #리스트로 반환
'''
# urljoin - URL을 합쳐주는 기능
'''
import urllib.parse

url = 'https://naver.com/a/b'

print(urllib.parse.urljoin(url, 'c'))
print(urllib.parse.urljoin(url, '/c'))
'''
# urljoin2
'''
import urllib.parse

url = 'https://naver.com/a/b/'

print(urllib.parse.urljoin(url, 'c'))
print(urllib.parse.urljoin(url, '/c'))
'''
# quote - 아스키 코드가 아닌 문자들을 퍼센트 인코딩으로 변환
'''
import urllib.request
from urllib import response

print(urllib.parse.quote('파이썬')) # 먼저 단어를 인코딩한 결과를 URL query에 복붙
URL = 'https://search.naver.com/search.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
response_urllib = urllib.request.urlopen(URL)
byte_data = response_urllib.read()
text_data = byte_data.decode()
print(text_data)
'''

# 파라미터를 변경해 여러 정보 가져오기
import urllib.parse
import urllib.request
import re

f = open("test2.txt",'w',encoding='UTF-8')
query_list = ['파이썬', '웹 크롤링', '빅데이터']
URL = 'https://search.naver.com/search.naver?query='

for i in query_list:
    new_URL = URL + urllib.parse.quote(i)
    response_urllib = urllib.request.urlopen(new_URL)
    byte_data = response_urllib.read()
    text_data = byte_data.decode()
    text_data = text_data.split('연관 검색어')[1].split('닫기')[1].split('더보기')[0]
    text_data = re.sub('<.+?>','',text_data,0,re.I|re.S)
    text_data = text_data.replace('  ',' ').strip()
    print(i, ":", text_data)

