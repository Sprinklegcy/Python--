#  @data   2020-04-26 19:00
import requests
from bs4 import BeautifulSoup
import os


def get_info(href):
    resp = requests.get(href)
    sp = BeautifulSoup(resp.text, "lxml")
    intro = sp.find('div', class_="intro")
    resume = ""
    for p in intro.find_all('p'):
        resume += str(p.string) + "\n"
    return resume


def get_photo(href):
    resp = requests.get(href)
    sp = BeautifulSoup(resp.text, "html.parser")
    img_url = sp.find('div', class_="info_img").img["src"]
    return requests.get("http://www.cae.cn" + img_url).content


try:
    os.mkdir("result")
except:
    pass
url = "http://www.cae.cn/cae/html/main/col48/column_48_1.html"
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, 'html.parser')

li = soup.find_all('li', class_="name_list")

base_url = "http://www.cae.cn"

for e in li:
    name = str(e.a.string)
    offset_url = e.a["href"]
    try:
        os.makedirs("result/" + name)
        with open("result/" + name + "/简介.txt", 'w', encoding='utf-8') as f:
            f.write(get_info(base_url + offset_url))
        # with open("result/" + name + "/照片.jpg", 'wb') as f:
        #     f.write(get_photo(base_url + offset_url))
    except FileExistsError as e:
        print(e)
    except Exception as ex:
        print(ex)



