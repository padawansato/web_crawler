# web_crawler
web crawler 習作

### 目的
Webクローラーを自作し，そのノウハウを習得する．

### ファイル構造
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
│   └── spiders		#クローラ本体の格納
│       ├── __init__.py
│       └── __pycache__
└── scrapy.cfg
```


### 参考および引用元
http://sssslide.com/speakerdeck.com/amacbee/pythondezuo-ruwebkuroraru-men