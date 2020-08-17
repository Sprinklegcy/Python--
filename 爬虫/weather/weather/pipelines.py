# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class WeatherPipeline(object):
    def __init__(self):
        self.f = open("weather.txt", 'w')

    def process_item(self, item, spider):
        print('======================')
        text = item['city'] + "\t" + item['date'] + "\t" + item['max_temperature'] + "\t" \
               + item['min_temperature'] + "\t" + item['weather'] + "\t" + item['wind'] + "\n"
        self.f.write(text)
        print(text)
        print('======================')
        return item

    def close_spider(self, spider):
        self.f.close()
