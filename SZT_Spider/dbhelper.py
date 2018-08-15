#coding:utf-8

import MySQLdb
from scrapy.utils.project import get_project_settings  # 引入settings配置


class DBHelper():

    def __init__(self):
        self.settings = get_project_settings()  # 获取settings配置数据

        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']

    # 连接mysql
    def connectMysql(self):
        conn = MySQLdb.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               charset='utf8')
        return conn

    # 连接数据库
    def connectDatabase(self):
        conn = MySQLdb.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.db,
                               charset='utf8')
        return conn

    # 创建数据库
    def createDatabase(self):
        conn = self.connectMysql()

        sql = "create database if not exists " + self.db
        cur = conn.cursor()
        cur.execute(sql)

        cur.close()
        conn.close()

    # 创建数据表
    def createTable(self, sql):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()

    # 插入数据
    def insert(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()  # 这里；是数据库操作语句结束符号
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    # 更新数据
    def update(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    # 删除数据
    def delete(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()


# 测试数据库操作
class TestDBHelper():
    def __init__(self):
        self.dbHelper = DBHelper()

    # 创建数据库
    def testCreateDatebase(self):
        self.dbHelper.createDatabase()

    # 创建表操作
    def testCreateTable(self):
        sql = "create table if not exists ticket_info(id int primary key auto_increment, card_no varchar(50), card_amt varchar(50), last_use_time datetime)"
        self.dbHelper.createTable(sql)

    # 插入数据，这里可以针对不同的表插入数据，piplines传递过来的item存储的是所有数据，可以分类插入不同的表
    # pymysql中也可以在这里对不同的表进行操作，不许需要考虑item数据的传递分类，根据自己的需要取就行，根据需要存即可
    def testInsert(self, item):
        sql = "insert into ticket_info(card_no, card_amt, last_use_time) values(%s, %s, %s)"
        params = (item['card_no'], item['card_amt'], item['last_use_time'])
        self.dbHelper.insert(sql, *params)

        # 更新操作
#     def testUpdate(self):
#         sql = "update testtable set name=%s,url=%s where id=%s"
#         params = ("update", "update", "1")
#         self.dbHelper.update(sql, *params)
#
#     def testDelete(self):
#         sql = "delete from testtable where id=%s"
#         params = ("1")
#         self.dbHelper.delete(sql, *params)
#

# 调用测试
# if __name__ == "__main__":
#     testDBHelper = TestDBHelper()
#     testDBHelper.testCreateDatebase()
#     testDBHelper.testCreateTable()
#     testDBHelper.testInsert()
#     testDBHelper.testUpdate()
#     testDBHelper.testDelete()