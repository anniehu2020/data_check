# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 16:58
# @Author  : annie.hu
# @FileName: __init__.py
"""数据库配置"""

'''测试环境'''
db_src = {
    'HOST': '127.0.0.1',
    'PORT': 3306,
    'USER': 'xxxx',
    'PASSWD': 'xxxxx',
    'DB': 'test',
}

db_supplier = {
    'HOST': '127.0.0.1',
    'PORT': 3306,
    'USER': 'xxxx',
    'PASSWD': 'xxxxx',
    'DB': 'test',
}

'''数据表格式化'''
SRC_TABLE = '{}.{}'.format(db_src['DB'], 't_order')
T_supplier_order = '{}.{}'.format(db_supplier['DB'], 't_test_order')
T_ADDRESS_INFO = '{}.{}'.format(db_src['DB'], 't_address_info')
T_AGENT_INFO = '{}.{}'.format(db_src['DB'], 't_agent_info')
T_ORDER_ACTIVITY_ER = '{}.{}'.format(db_src['DB'], 't_test_activity')
