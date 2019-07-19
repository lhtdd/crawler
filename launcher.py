#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
from crawler import qiushibaike_crawler as qb


if __name__ == '__main__':
    # 创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    # 添加任务,时间间隔10m
    scheduler.add_job(qb.crawler_leisure, 'interval', minutes=10, id='qiushi_crawler_leisure_job')
    scheduler.start()
