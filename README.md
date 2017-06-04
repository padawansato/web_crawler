# web_crawler
web crawler 習作

## 目的
Webクローラーを作成し，そのノウハウを習得する．
キーワード:scrapy,

### 参考および引用元
PyConJP2016
Pythonで作るWebクローラ入門 発表者 真嘉比 愛（Ai Makabi）
http://sssslide.com/speakerdeck.com/amacbee/pythondezuo-ruwebkuroraru-men


#### クローリング対象
www.python.org/jobs
上記ページに表記されている，"募集内容","勤務地","企業名"の情報をクローリングする．

#### scrapy とは
python	    クローラフレームワーク

#### scrapy ファイル構造
```
/Users/e155755/Desktop/web_crawler/my_pyjob% tree -L 3
.
├── my_pyjob
│   ├── __init__.py
│   ├── __pycache__
│   ├── items.py		#クロールする対象について
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders			#クローラ本体の格納
│       ├── __init__.py
│       └── __pycache__
└── scrapy.cfg
```


### クローラの作成手順
#### クローラーのひな形の生成
scrapy genspider コマンドで雛形となるクローラ（spider）を自動的に作成する．
`
%scrapy genspider クローラ名 クロール対象ドメイン
`

`
%scrapy genspider my_pyjob_spider python.org
`

`
/Users/e155755/Desktop/web_crawler/my_pyjob% less my_pyjob/spiders/my_pyjob_spider.py 
`


```
# -*- coding: utf-8 -*-
import scrapy


class MyPyjobSpiderSpider(scrapy.Spider):
    name = 'my_pyjob_spider'
    allowed_domains = ['python.org']
    start_urls = ['http://python.org/']

    def parse(self, response):
        pass

```