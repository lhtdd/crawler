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
    for i in range(1, 656):
        this_url = "http://www.33531.com/kxxh/list_15_"+str(i)+".html"
        crawler = base_crawler.Crawler()
        data = crawler.crawl_data(this_url, 'GBK')
        pat = r'<div class="text">(.*?)</div>'
        rst = re.compile(pat, re.S).findall(data)
        leisure = LeisureService()
        for j in range(0, len(rst)):
            has_all = rst[j].strip()
            content = ''
            if re.search('<span style="', has_all, re.I):
                pat_1 = '<span style="color.*?>(.*?)</span>'
                rst_1 = re.compile(pat_1, re.S).findall(has_all)
                for i in range(0, len(rst_1)):
                    content += rst_1[i].strip()+'<br/>'
            elif re.search('<p>', has_all, re.I):
                rst_2 = re.sub('(?:<p>|</p>|<div>|</div>)', '', has_all)
                content = rst_2.strip()
            print(content)
            print("==============")
            leisure.add_happiness(random.choice(crawler_params.customer_pools), content, 1, 4)
        time.sleep(5)


crawler_leisure()
