# <selenium 모듈>

# 뉴스스탠드 프린트하기
# find_element_by_id()
'''
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.naver.com')

element = driver.find_element_by_id("newsstand")
#print(element.tag_name)
print(element.text)
'''
# 오늘 읽을만한 글 카테고리 프린트하기
# find_element_by_class_name()
'''
from xml.dom.minidom import Element
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.naver.com')

element = driver.find_element_by_class_name("list_category_wrap")
print(element.tag_name)
print(element.text)
'''
# 이벤트로 제어하기 : click()
# 네이버 사전 클릭하기
'''
from xml.dom.minidom import Element
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.naver.com')

element = driver.find_element_by_class_name("NM_FAVORITE_LIST").find_element_by_css_selector("[data-clk='svc.dic']")
print(element)
element.click()
while True:
    q = input()
    if q == 'q':
        break
'''
# time 모듈을 사용하여 텀을 두고 실행하기
# 네이버 사전에서 한자사전 들어가기
'''
from xml.dom.minidom import Element
import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.naver.com')
time.sleep(2)

element = driver.find_element_by_class_name("NM_FAVORITE_LIST").find_element_by_css_selector("[data-clk='svc.dic']")
time.sleep(2)
element.click()
time.sleep(2)
element = driver.find_element_by_id("_id_hanja_href")
time.sleep(2)
element.click()
while True:
    q = input()
    if q == 'q':
        break
'''
# send_keys : key 입력
# Keys.ENTER : enter 동작
# 네이버에 웹 크롤링 검색하여 들어가기
'''
from xml.dom.minidom import Element
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.naver.com')

element = driver.find_element_by_id("query")
element.send_keys("웹 크롤링")
element.send_keys(Keys.ENTER)
while True:
    q = input()
    if q == 'q':
        break
'''
'''
import requests
from bs4 import BeautifulSoup
import selenium 
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.dhlottery.co.kr/gameResult.do?method=statByNumber')

table = driver.find_element_by_class_name('tbl_data_col')
tbody = table.find_element_by_tag_name("tbody")
'''



