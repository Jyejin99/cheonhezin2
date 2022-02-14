#4번 : 좋아하는 게임 캐릭터 정보 검색하기

import requests as req

f = open("test.html",'w',encoding='UTF-8')
cha_lst = ["89", "59", "1"]
URL = 'https://lol.inven.co.kr/dataninfo/champion/detail.php?detail.php'
game_cha=int(input("챔피언을 선택해주세요(0:아리, 1:소나, 2:아칼리) "))
pm = {'code':cha_lst[game_cha]}
response = req.get(URL,params=pm)
print(response.status_code)
html_source = response.text
f.write(html_source)
f.close()