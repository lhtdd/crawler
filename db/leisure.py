#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from db.lyao_db import LyaoDB
import time
import traceback


class LeisureService():
    def __init__(self):
        self.lyaoDB = LyaoDB()

    def query_happiness(self):
        sql = '''select * from t_happy'''
        try:
            self.lyaoDB.execute(sql)
            happiness = self.lyaoDB.cur.fetchall()
            print(happiness)
        except Exception as e:
            print('执行sql异常:', traceback.format_exc())

    def valid_check_happy(self, happy_text):
        if len(happy_text) <= 10:
            return False
        else:
            top_text = happy_text[:10]
            sql = """select count(1) from t_happy as a where a.happyText like '%s'"""
            data = top_text + '%'
            try:
                self.lyaoDB.execute(sql % data)
                self.lyaoDB.db.commit()
                count = self.lyaoDB.cur.fetchone()
                print(count)
                if count[0] == 0:
                    return True
                else:
                    return False
            except Exception as e:
                print('执行sql异常:', traceback.format_exc())
                self.lyaoDB.db.rollback()
                return False

    def add_happiness(self, customer_id, happy_text, status, resource):
        sql = """insert into t_happy(customerID,happyText,status,inTime,resource)
        values('%s','%s','%s','%s','%s')"""
        in_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data = (customer_id, happy_text, status, in_time, resource)
        try:
            self.lyaoDB.execute(sql % data)
            self.lyaoDB.db.commit()
            row_count = self.lyaoDB.cur.rowcount
            print(row_count)
        except Exception as e:
            print('执行sql异常:', traceback.format_exc())
            self.lyaoDB.db.rollback()
