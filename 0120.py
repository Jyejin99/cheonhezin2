
'''
import requests

URL = "https://www.naver.com"
response = requests.get(URL)
html_data = response.text

import re
f = open("test2.txt",'w',encoding='UTF-8')
body = re.search('<div class="group_theme".*<div class="group_theme _NM_API_UI',html_data, re.I|re.S)
body = body.group()
body = re.sub('<.+?>','',body)
body = re.sub('이미지 준비중','',body)
body = body.split('p class')[0]

print(body)
f.write(body)
f.close()
'''

