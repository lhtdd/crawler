#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib.request
import random
from config import crawler_params


class Crawler():

    def ua(self):
        opener = urllib.request.build_opener()
        this_ua = random.choice(crawler_params.ua_pools)
        ua = ("User-Agent", this_ua)
        opener.addheaders = [ua]
        urllib.request.install_opener(opener)
        print("当前使用UA：" + str(this_ua))

    def crawl_data(self, url, charset):
        self.ua()
        print("抓取地址：" + str(url))
        data = urllib.request.urlopen(url).read().decode(charset, "ignore")
        return data
