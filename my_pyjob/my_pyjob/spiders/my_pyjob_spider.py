# -*- coding: utf-8 -*-
import scrapy


class MyPyjobSpiderSpider(scrapy.Spider):
    name = 'my_pyjob_spider'
    allowed_domains = ['python.org']
    start_urls = ['http://python.org/']

    def parse(self, response):
        pass
