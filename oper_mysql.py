# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 16:10
# @Author  : annie.hu
# @FileName: oper_mysql.py
"""
    需要插入要求的数据，作为大数据量统计测试用，考虑使用 存储过程 产生数据无规律，选择使用python的 pymysql操作数据库完成数据插入
    编程思路：面向对象 + 模块化 编写
"""
import pymysql


class OperMysql:
    def __init__(self, HOST, PORT, USER, PASSWD, DB, CHARSET='utf8mb4'):
    # def __init__(self, HOST, PORT, USER, PASSWD, DB, CHARSET='utf8'):
        try:
            self.conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception as e:
            print('数据库连接失败！')
            print(e)

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    def executemany(self, sql, args):
        """参数化执行目标sql"""
        self.cursor.executemany(sql, args)
        self.conn.commit()

    def get_db_data(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    db_conf = {
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'XXXXX',
        'PASSWD': 'XXXX',
        'DB': 'XXXXXX',
    }
    sql = "select * from feeds.491302518131789824_card_event limit 1;"

    op = OperMysql(**db_conf)
    op.execute(sql)
    data = op.get_db_data()
    op.close()

    print(data)
