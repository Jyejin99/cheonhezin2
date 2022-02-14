# 인기 뉴스 출력하기

from email import header
import requests
import re

f = open("test2.txt",'w',encoding='UTF-8')
URL = "https://media.naver.com/press/005/ranking"
pm = {"type":"popular"}
response = requests.get(URL,pm)
html_data = response.text

#print(html_data.find('<ul class="press_ranking_list">'))
temp = html_data[56798:70000]

body = re.search('<li class="as_thumb".*',temp, re.I|re.S)
body = body.group()
body = re.sub('<.+?>','',body)
body = body.replace(" ","")
for i in range(5):
    body = body.replace("\n\n","\n")

print(body.split("<"))
f.write(body.split("<")[0])
f.close()