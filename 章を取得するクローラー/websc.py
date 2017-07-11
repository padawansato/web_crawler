# coding: UTF-8
# ポケモンの名前を取得したい　https://www.buzzfeed.com/awesomer/the-definitive-ranking-of-the-original-151-pokemon?utm_term=.qiJzp8b49#.cmOXMq4kV
# 参考　http://qiita.com/Azunyan1111/items/9b3d16428d2bcc7c9406

import urllib2
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://www.buzzfeed.com/awesomer/the-definitive-ranking-of-the-original-151-pokemon?utm_term=.fb10WXwdP#.bf2aLRmDJ"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# span要素全てを摘出する→全てのspan要素が配列に入ってかえされます→[<span class="m-wficon triDown"></span>, <span class="l-h...
span = soup.find_all("span")

# print時のエラーとならないように最初に宣言しておきます。
nikkei_heikin = ""
# for分で全てのspan要素の中からClass="hoge"となっている物を探します
for tag in span:
    # classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
    try:
        # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
        string_ = tag.get("class").pop(0)

        # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
        if string_ in "js-subbuzz__title-text":
            # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
            nikkei_heikin = tag.string
            # 摘出が完了したのでfor分を抜けます
#            break
            print nikkei_heikin
    except:
        # パス→何も処理を行わない
        pass

# 摘出した日経平均株価を出力します。
print nikkei_heikin

