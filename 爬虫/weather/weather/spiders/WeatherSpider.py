# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
import re
import random
from weather.items import WeatherItem

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


def get_city_href():
    url = "http://lishi.tianqi.com/"
    html = requests.get(url, headers=headers).text  # 获取html内容
    soup = BeautifulSoup(html, "html.parser")  # 煲一锅汤
    result_list = soup.find_all('a', target='_blank', href=re.compile(r'\A[a-z]+/index.html'))  # 得到所有target="_blank"的 <a> 标签
    href_list = list()
    for e in result_list:
        href_list.append(e['href'].split('/')[0])  # 得到 <a> 标签的 href 属性, 切片，得到城市名拼音
    href_list.append('suyouqi')  # 前两个城市格式和其他的不一样，手动添加进去
    href_list.append('zhurihe')  # 前两个城市格式和其他的不一样，手动添加进去
    return href_list

class WeatherspiderSpider(scrapy.Spider):
    name = 'WeatherSpider'
    # allowed_domains = ['www.baidu.com']
    base_url = "http://lishi.tianqi.com/"
    offset = ""
    start_urls = [base_url + offset]

    def parse(self, response):
        try:
            node_list = response.xpath('//ul[@class="lishitable_content clearfix"]/li')
            for node in node_list:
                item = WeatherItem()
                item["city"] = response.xpath("//div[@class='linegraphborder'][2]/div[@class='linegraphbox']/div"
                                              "[@class='linegraphtitle']").extract()[0].split('\n')[1]  #
                item["date"] = node.xpath("./div[1]/text()").extract()[0]
                item["max_temperature"] = node.xpath("./div[2]/text()").extract()[0]
                item["min_temperature"] = node.xpath("./div[3]/text()").extract()[0]
                item["weather"] = node.xpath("./div[4]/text()").extract()[0]
                item["wind"] = node.xpath("./div[5]/text()").extract()[0]
                yield item
        except:
            print("error")
            yield
        for city in get_city_href():
            for year in range(2011, 2019):
                for month in range(1, 13):
                    url = self.base_url + str(city) + "/" + str(year) + "{:0>2d}".format(month) + ".html"
                    yield scrapy.Request(url, callback=self.parse)


