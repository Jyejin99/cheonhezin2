from email.mime import application
from tkinter import Variable
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import time as t

f = open("test.html",'w',encoding='utf-8')
req = requests.get("https://www.dhlottery.co.kr/gameResult.do?method=statByNumber")
html = req.text
soup = BeautifulSoup(html, "html.parser")
contents = soup.find('body')
lstPrint = []
tag = contents.find("table", class_="tbl_data tbl_data_col")

for i in tag.find_all("tr"):
    lst = []    
    for z in i.find_all("td"):
        info = z.get_text()
        numbers = re.findall('\d+',info)
        lst.append(int(numbers[0]))
    if len(lst) > 0:
        lstPrint.append(lst)
#print(lstPrint)

sum = 0

for i in lstPrint:
    sum += i[2]
#print(sum)

np.random.seed(int(t.time()))
per = []

for i in lstPrint:
    per.append(round(i[2]/sum,3))

#print(per)

a = np.arange(1,46)

f.write("<html>\n")
f.write("\t<head>\n")
f.write("</head>\n")
f.write("\t<body>\n")
f.write("\t\t<div>{0}회차 예상 번호\n".format(round((sum/7)+1)))
# for i in range(5):
#     b = np.random.choice(a,6,replace=False, p =per)
#     b = np.sort(b)
#     f.write("\t\t\t<div>\n")
#     f.write("\t\t\t\t")
#     for i in b:
#         f.write(str(i)+" ")
#     f.write("\n")
#     f.write("\t\t\t</div>\n")
# f.write("\t\t</div>\n")
# f.write("\t</body>\n")
# f.write("<html>")
# f.close()

    
for i in range(5):
    b = np.random.choice(a,6,replace=False, p =per)
    b = np.sort(b)
    f.write("\t\t\t<div>\n")
    f.write("\t\t\t\t")
    for i in b:
        f.write('<div style="width:100px;height:100px;border:1pt solid #440088;border-radius:50px;filter:alpha(opacity=30);opacity:0.3;background:#bbff88;float:left">')
        f.write(str(i)+" ")
        f.write("</div>")
    f.write("\n")
    f.write("\t\t\t</div>\n")
f.write("\t\t</div>\n")
f.write("\t</body>\n")
f.write("<html>")
f.close()
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=mjy9088&logNo=30182385149