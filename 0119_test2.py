#2번 : 오늘의 날씨 구하기
'''
import requests

f = open("test.html",'w',encoding='UTF-8')
weather = input("날씨를 알고싶은 지역을 입력해주세요: ")
URL = 'https://search.naver.com/search.naver'
pm = {'query':weather+' 날씨'}
response = requests.get(URL,params=pm)
print(response.text)
html_source = response.text
f.write(html_source)
f.close()
'''
import requests

area = ["아산시 탕정면","수원시 권선구","화성시 남양읍"]
area_lst = {area[0]:"15200330", area[1]:"02113133", area[2]:"02590262"}

f = open("test.html",'w',encoding='UTF-8')
URL = 'https://weather.naver.com/today'
user = int(input("원하는 지역을 선택해주세요(0:아산시 탕정면, 1:수원시 권선구, 2:화성시 남양읍"))
#pm = {'titleId':area_lst[area[user]]}
URL = URL+"/"+area_lst[area[user]]
response = requests.get(URL)
print(response.status_code)
html_source = response.text
f.write(html_source)
f.close()
