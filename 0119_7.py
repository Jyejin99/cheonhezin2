import requests

f = open("test2.html",'w',encoding='UTF-8')
URL = 'https://comic.naver.com/webtoon/detail.nhn'
params = {'titleId':748105, 'no':101}
response = requests.get(URL,params=params)
print(response.text)
html_source = response.text
f.write(html_source)
f.close()