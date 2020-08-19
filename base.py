# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 16:47
# @Author  : annie.hu
# @FileName: data.py
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__name__)))
import time

from oper_mysql import OperMysql
from setting import *
from logUtil import LogUtils


class Data:
    count = 0

    @staticmethod
    def db_conn():
        op = OperMysql(**db_src)
        return op

    @staticmethod
    def thread_init(thread_id, log=LogUtils):
        """线程级别初始化"""
        start_time = time.time()
        log.info("开始时间：{}，线程名：{}".format(start_time, thread_id))
        op = OperMysql(**db_src)
        op_supplier = OperMysql(**db_supplier)
        # op_user与crm库同host
        # op_user = OperMysql(**db_user) if hasattr(setting, 'db_user') else op_crm
        return op, op_supplier, start_time

    @staticmethod
    def thread_teardown(thread_id, op, start_time, log=LogUtils, op_crm=None, op_user=None):
        op.close()
        if op_crm:
            op_crm.close()
        if op_user:
            op_user.close()
        stop_time = time.time()
        log.info("结束时间：{}，线程名：{}，线程耗时：{:.2f} s".format(stop_time, thread_id, stop_time - start_time))






