# -*- coding:utf-8 -*-
import pymysql
from DBUtils.PooledDB import PooledDB


class LyaoDB():
    def __init__(self):
        self.host = '39.105.172.254'
        self.instance = 'mo'
        self.port = 3306
        self.user = 'root'
        self.passwd = 'mo1234567'
        self.pool = PooledDB(pymysql, 5, host=self.host, port=self.port, db=self.instance, user=self.user,
                             passwd=self.passwd, setsession=['SET AUTOCOMMIT = 1'])

    # 连接数据库
    def connect_db(self):
        self.db = self.pool.connection()
        self.cur = self.db.cursor()

    # 关闭连接
    def close_db(self):
        self.cur.close()
        self.db.close()

    # 执行sql
    def execute(self, sql):
        print('执行SQL:', sql)
        self.connect_db()
        return self.cur.execute(sql)

