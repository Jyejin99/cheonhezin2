# 뉴스 랭킹 워드클라우드로 출력하기

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
    if i.text == "뉴스":
        element = i
element.click()
time.sleep(1)

elements_ranking = driver.find_elements_by_class_name("Nitem_link")
for i in elements_ranking:
    if i.text == "랭킹":
        element_ranking = i
element_ranking.click()
time.sleep(1)

lst = []
count = 0
elements_data = driver.find_elements_by_class_name("rankingnews_box")
for i in elements_data:
    titles = i.find_elements_by_class_name("rankingnews_name")
    contents = i.find_elements_by_class_name("rankingnews_list")
    for j in titles:
        #print(j.text)
        news_no = 1
        for k in contents:
            cons = k.find_elements_by_class_name("list_content") 
            for l in cons:
                con = l.find_element_by_tag_name('a')
                #print(news_no,":",con.text)
                lst.append(con.text)
                news_no+=1
    if count == 11:
        break
    count+=1

txt = " ".join(lst)
print(txt)

world_mask = np.array(Image.open('korea.JPG'))

wdcloud = wc(font_path='malgun', background_color="white", max_words=700, max_font_size=800, mask=world_mask).generate(txt)
plt.figure(figsize=(200,200))
plt.imshow(wdcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
'''
import selenium
import time
from selenium import webdriver

path = 'chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://www.naver.com')

elements = driver.find_elements_by_class_name("nav")
for i in elements:
    if i.text == "뉴스":
        element = i
element.click()

elements_ranking = driver.find_elements_by_class_name("Nitem_link")
for i in elements_ranking:
    if i.text == "랭킹":
        element_ranking = i
element_ranking.click()

count = 0
elements_data = driver.find_elements_by_class_name("rankingnews_box")
for i in elements_data:
    titles = i.find_elements_by_class_name("rankingnews_name")
    contents = i.find_elements_by_class_name("rankingnews_list")
    for j in titles:
        print(j.text)
        news_no = 1
        for k in contents:
            cons = k.find_elements_by_class_name("list_content") 
            for l in cons:
                con = l.find_element_by_tag_name('a')
                print(news_no,":",con.text)
                news_no+=1
    if count == 11:
        break
    count+=1
    '''