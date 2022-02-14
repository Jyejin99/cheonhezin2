# 뉴스 랭킹 워드클라우드로 출력하기2
'''
from importlib.resources import contents
import selenium
import time
from selenium import webdriver
from wordcloud import WordCloud as wc
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

path = 'chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://www.naver.com')

elements = driver.find_elements_by_class_name("nav")
for i in elements:
    if i.text == "증권":
        element = i
element.click()
time.sleep(1)

elements_news = driver.find_elements_by_class_name("m7")
for i in elements_news:
    if i.text == "뉴스":
        element_ranking = i
element_ranking.click()
time.sleep(1)

lst = []

count = 0
elements_data = driver.find_elements_by_class_name("summary_block")
for i in elements_data:
    titles = i.find_elements_by_class_name("tit")
    content = i.find_elements_by_css_selector("ul > li")
    for z in titles:
        print("<", z.text, ">")
        for a in content:
            print(a.text)
            lst.append(a.text)

txt = " ".join(lst)

world_mask = np.array(Image.open('korea.JPG'))

wdcloud = wc(font_path='malgun', background_color="white", max_words=700, max_font_size=800, mask=world_mask).generate(txt)
plt.figure(figsize=(200,200))
plt.imshow(wdcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

q = input()
while True:
    if q==q:
        break
'''

from importlib.resources import contents
import selenium
import time
from selenium import webdriver
from wordcloud import STOPWORDS, WordCloud as wc
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

path = 'chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://www.naver.com')

elements = driver.find_elements_by_class_name("nav")
for i in elements:
    if i.text == "증권":
        element = i
element.click()
time.sleep(1)

elements_news = driver.find_elements_by_class_name("m7")
for i in elements_news:
    if i.text == "뉴스":
        element_ranking = i
element_ranking.click()

lst = []

time.sleep(1)
element_news2 = driver.find_element_by_class_name("tlt_more")
element_news2.click()

count = 0
elements_data = driver.find_elements_by_class_name("block1.clearfix")
for i in elements_data:
    content = i.find_elements_by_css_selector("ul > li > a")
    for a in content:
        print(a.text)
        lst.append(a.text)

txt = " ".join(lst)
print(txt)
world_mask = np.array(Image.open('korea.JPG'))

wdcloud = wc(font_path='malgun', background_color="white", max_words=700, max_font_size=800, mask=world_mask).generate(txt)
plt.figure(figsize=(200,200))
plt.imshow(wdcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

q = input()
while True:
    if q==q:
        break
