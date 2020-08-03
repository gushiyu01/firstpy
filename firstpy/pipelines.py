# -*- coding: utf-8 -*-
import pymysql
from twisted.enterprise import adbapi
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FirstpyPipeline(object):

    def __init__(self, dbpool):

        self.dbpool = dbpool
        print("数据库连接成功")

    @classmethod
    def from_settings(cls, settings):   # 函数名固定会被scrapy调用，直接keyongsettings的值
        adbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DB'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            cursorclass=pymysql.cursors.DictCursor,
            charset='utf8',
            use_unicode=True
        )

        #   连接数据池ConnectionPool，使用pymysql连接
        dbpool = adbapi.ConnectionPool('pymysql', **adbparams)

        # 返回实例化参数
        return cls(dbpool)

    def process_item(self, item, spider):
        #   使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        query = self.dbpool.runInteraction(self.do_insert, item)    # 指定操作方法和操作数据
        #   添加异常处理
        query.addCallback(self.handle_errors)

        return item

    def do_insert(self, cursor, item):
        #   对数据库进行插入操作，并不需要commit，twisted会自动commit
        insert_sql = """
        insert into poem(id, poem_author, poem_title, poem_dynasty, poem_content, poem_pic_url, poem_type) values (%s, %s, %s, %s, %s, %s, "爱情诗");
        """
        cursor.execute(insert_sql, (item['id'], item['poemAuthor'], item['poemTitle'], item['poemDynasty'], item['poemContent'], item['poemPicUrl']))

    def handle_errors(self, failure):
        if failure:
            #   打印错误信息
            print(failure)
            print("出错了")
