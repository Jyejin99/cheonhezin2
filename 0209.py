html = """
<html>
    <head>
            <title>crawl</title>
    </head>
    <body>
        <p class="a" align="center"> text1 </p>
        <p class="b" align="center"> text2 </p>
        <p class="c" align="center"> text3 </p>
        <div>
            <img arc="/source" width="300" height="200">
        </div>
    </body>
</html>"""

# 노드를 활용한 검색
'''
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
contents = soup.find('body')

# 자식 노드들을 반복 가능한 객체로 반환
for child in contents.children:
     print(child) 

# 자신을 포함한 부모 노드까지 출력
img_tag = contents.find('img')
print(img_tag)
print(img_tag.parent)

# find_next_sibling(): 바로 다음 형제 노드를 검색
# find_next_siblings(): 모든 형제 노드를 검색
p_tag = contents.find("p", class_="b")
print(p_tag)

print(p_tag.find_next_sibling())
print(p_tag.find_next_siblings())
'''

# Naver 로그인 하기
# 이 방법은 네이버가 자동입력방지를 도입하여 현재는 할 수 없음
'''
import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.naver.com')

element = driver.find_element_by_class_name("link_login")
element.click()
id = 'jheil339'
pw = ' '
element = driver.find_element_by_id('id')
element.send_keys(id)
time.sleep(1)
element = driver.find_element_by_id('pw')
element.send_keys(pw)
time.sleep(1)
element = driver.find_element_by_class_name('btn_login')
element.click()

q = input()
while True:
    if q==q:
        break

'''
# 네이버 메일 제목 가져오기
'''
from xml.dom.minidom import Element
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.naver.com')

element = driver.find_element_by_class_name("link_login")
element.click()
id = 'jheil339'
pw = ' '
num = ' '
driver.execute_script("document.getElementById('id').value=\'" + id + "\'")
time.sleep(1)
driver.execute_script("document.getElementById('pw').value=\'" + pw + "\'")
time.sleep(1)

element = driver.find_element_by_class_name('btn_login')
element.click()
time.sleep(1)

driver.execute_script("document.getElementById('phone_value').value=\'" + num + "\'")
time.sleep(1)
element = driver.find_element_by_class_name('int_ok')
element.click()
time.sleep(1)
element = driver.find_element_by_id('new.dontsave')
element.click()
time.sleep(1)
driver.get('https://mail.naver.com/')

page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
#print(soup)

mail_list = soup.find_all('strong', class_="mail_title")
for title in mail_list:
    print(title.text)

# print(mail_list.select_one('a').text)
# print(mail_list.select_one('strong').text)

q = input()
while True:
    if q==q:
        break
'''