# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class MyPyjobSpiderSpider(scrapy.Spider):
    name = 'my_pyjob_spider'
    allowed_domains = ['python.org'] #クローリング対象ドメイン
    start_urls = ['http://python.org/jobs/']



    def parse(self, response): 
        # ページ中のジョブオファー情報を全て取得 
        soup = BeautifulSoup(response.body)
        links = soup.find_all('a')
        for link in links:
        h2 = soup.find('h2', id="listing-company")
        a_tag = h2.a
        a_string = a_tag.string
        print a_string
        job['title'] = soup.find('a', id="href")
            


        # beautifulsoupを用いる場合

      # 次のページへのリンクが入った <li> を取得する
        next_page = soup.find('li', {'class': 'next'})
        # <li> の中に入った <a> を取り出す
        next_page_link = next_page.a
        # 次のページがあるか確認する
        if 'href' not in next_page_link.attrs:
            # 次のページが見つからなかったので終了
            yield

        # 次のページがあるときは URL を組み立てる
        baseurl = 'https://www.python.org/jobs/'
        path = next_page_link['href']
        url = '{baseurl}{path}'.format(baseurl=baseurl, path=path)
        print(url)

        # scrapy.Request を返すと次にクロールするページの指定になる
        next_crawl_page = scrapy.Request(url)
        yield next_crawl_page


        # beautifulsoupを用いない場合の例
        # for res in response.xpath("//h2[@class='list..."):

        #     job = PyjobItem() 
        #     job['title'] = res.xpath(".//span[@cla...")... 
        #     job['company'] = res.xpath(".//span[@cla...")... 
        #     job['location'] = res.xpath(".//a[start...")... 
        #     yield job 

            # # 「Next」のリンクを取得してクロールする 
            # next_page = response.xpath("//li[@cla...").extract() 
            # if next_page: 
            #     url = response.urljoin(next_page[0]) 
            #     yield scrapy.Request(url, callback=self.parse)

                
