#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
from crawler import base_crawler
import random
import time
from config import crawler_params
from db.leisure import LeisureService
from apscheduler.schedulers.blocking import BlockingScheduler


def crawler_leisure():
    for i in range(1, 14):
        this_url = "https://www.qiushibaike.com/text/page/"+str(i)
        crawler = base_crawler.Crawler()
        data = crawler.crawl_data(this_url, 'utf-8')
        pat = r'<div class="article.*?id=\'qiushi_tag_(.*?)\'>.*?<div class="content">.*?<span>(.*?)</span>(.*?)</div>'
        rst = re.compile(pat, re.S).findall(data)
        leisure = LeisureService()
        for j in range(0, len(rst)):
            has_all = rst[j][2].strip()
            if re.search('contentForAll', has_all, re.I):
                content_num = rst[j][0].strip()
                article_url = "https://www.qiushibaike.com/article/" + content_num
                article_data = crawler.crawl_data(article_url, 'utf-8')
                article_pat = r'<div class="content">(.*?)</div>'
                article_rst = re.compile(article_pat, re.S).findall(article_data)
                content = article_rst[0]
            else:
                content = rst[j][1].strip()
            print(content)
            print('==============')
            if leisure.valid_check_happy(content):
                leisure.add_happiness(random.choice(crawler_params.customer_pools), content, 1, 3)
            else:
                print('已存在，不入库')
        time.sleep(5)


# 创建调度器：BlockingScheduler
scheduler = BlockingScheduler()
# 添加任务,时间间隔10m
scheduler.add_job(crawler_leisure, 'interval', minutes=10, id='qiushi_crawler_leisure_job')
scheduler.start()
