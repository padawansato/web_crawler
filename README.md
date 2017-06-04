# web_crawler
web crawler 習作

### 目的
Webクローラーを作成し，そのノウハウを習得する．

### 参考および引用元
PyConJP2016
Pythonで作るWebクローラ入門 発表者 真嘉比 愛（Ai Makabi）
http://sssslide.com/speakerdeck.com/amacbee/pythondezuo-ruwebkuroraru-men


#### クローリング対象
www.python.org/jobs
上記ページに表記されている，"募集内容","勤務地","企業名"の情報をクローリングする．

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


