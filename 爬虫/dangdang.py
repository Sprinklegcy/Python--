#  @data   2019/12/8 22:42
#  @data   2019/12/4 15:02

import requests
from bs4 import BeautifulSoup
import random
import bs4

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
headers = {'User-Agent': random.choice(my_headers)}

# url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1"  # 书名，评论数，作者，价格

base_url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-"

with open('books.txt', 'w', encoding="utf-8-sig") as f:
    for count in range(1, 26):
        url = base_url + str(count)

        r = requests.get(url, headers=headers)
        r.encoding = 'gb2312'
        soup = BeautifulSoup(r.text, "html.parser")

        li = soup.find('ul', class_="bang_list clearfix bang_list_mode").find_all('li')

        for item in li:
            name = item.find('div', class_="name").a.attrs['title'].split('（')[0]  # 取消这行注释得到的就是简洁书名
            publisher = item.find('div', class_="publisher_info").a.string
            comment_num = item.find('div', class_="star").a.string.replace("条评论", "")
            price = item.find('div', class_="price").p.find('span', class_="price_n").string

            print(name, publisher, comment_num, price)
            f.write(name + '\t\t' + publisher + '\t\t' + comment_num + '\t\t' + price + "\n")


# print(li)
# print(len(li))