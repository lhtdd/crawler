#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib.request
import re
from crawler import base_crawler
import random
import time
from config import crawler_params
from db.leisure import LeisureService


for i in range(1, 2):
    this_url = "https://www.qiushibaike.com/text/page/"+str(i)
    crawler = base_crawler.Crawler()
    data = crawler.crawl_data(this_url, 'utf-8')
    pat = r'<div class="article block.*?id="qiushi_tag_(.*?)">.*?<div class="content">.*?<span>(.*?)</span>(.*?)</div>>'
    rst = re.compile(pat, re.S).findall(data)
    print(len(rst))
    leisure = LeisureService()
    for j in range(0, len(rst)):
        print(rst[j][0].strip())
        print(rst[j][1].strip())
        has_all = rst[j][2].strip()
        if re.search('contentForAll', has_all, re.I):
            contentNum = rst[j][0].strip()
            article_url = "https://www.qiushibaike.com/article/" + contentNum
            article_data = crawler.crawl_data(article_url, 'utf-8')
            article_pat = r'<div class="content">(.*?)</div>'
            article_rst = re.compile(article_pat, re.S).findall(article_data)
            content = article_rst[0]
        else:
            content = rst[j][1].strip()
        print(content)
        print("==============")
        #leisure.add_happiness(random.choice(crawler_params.customer_pools), content, 1, 3)
    #time.sleep(5)
