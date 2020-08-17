#  @data   2020-04-26 16:58
import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"

response = requests.get(url)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")

th = ["排名", "学校名称", "省市", "总分", "生源质量（新生高考成绩得分）"]

for elem in soup.find_all('tr', class_="alt")[:50]:
    print("{:^4}".format(elem.find_all("td")[0].string), end='')
    for e in elem.find_all("td")[1:4]:
        print("{1:{0:}^10}".format(chr(12288), e.string), end='')
    print("{:^4}".format(elem.find_all("td")[4].string), end='')
    print()
