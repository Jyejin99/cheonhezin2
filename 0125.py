'''
import selenium

print(selenium.__version__)
'''

import selenium
from selenium import webdriver

#path = "C:\\Users\\user\\Desktop\\html_code\\chromedriver.exe"
#driver = webdriver.Chrome(path)
driver = webdriver.Chrome()
driver.get('https://www.naver.com')
# 까지 쓰면 바로 프로그램 종료되기 때문에 다른 실행되는 함수 작성해줌
while True:
    q = input()
    if q == 'q':
        break
