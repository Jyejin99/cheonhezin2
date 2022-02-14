import requests as req

f = open("test.html",'w',encoding='UTF-8')
URL = 'https://search.naver.com/search.naver'
pm = {'query':'선문대학교'}
response = req.get(URL, params=pm)
print(response.status_code)
html_source = response.text
f.write(html_source)
f.close()