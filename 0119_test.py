#1번 요일별 원하는 웹툰
import requests
import datetime as dt

today = dt.datetime.today().weekday()
days = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
webtoon_lst = {days[0]:"183559", days[1]:"784248",days[2]:"738694", days[3]:"747271",days[4]:"773797",days[5]:"773796",days[6]:"774044"}

f = open("test.html",'w',encoding='UTF-8')
URL = 'https://comic.naver.com/webtoon/detail.nhn'
pm = {'titleId':webtoon_lst[days[today]]}
response = requests.get(URL,params=pm)
print(response.status_code)
html_source = response.text
f.write(html_source)
f.close()