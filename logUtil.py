# -*- coding: utf-8 -*-
# @Time    : 2020/4/08 9:47
# @Author  : annie.hu
# @FileName: logUtil.py

import logging
import logging.config
import os


class LogUtils:
    logger = None
    log_dir = r'../log/'     # log目录，相对运行文件创建
    # run_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # log_path = os.path.join(run_dir, r"log/")
    # log_conf_dir = os.path.join(run_dir, "conf")
    # log_conf_file = os.path.join(log_conf_dir, "logging.ini")

    def __init__(self, log_name):
        os.makedirs(self.log_dir) if not os.path.exists(self.log_dir) else None
        self.logger = logging.getLogger(log_name)
        # 设置日志默认级别
        self.logger.setLevel(logging.DEBUG)

        # 初始化handler
        file_handler = logging.FileHandler(filename=os.path.join(self.log_dir, log_name), mode="w", encoding='utf-8')
        stream_handler = logging.StreamHandler()

        # 设置输出格式
        famtter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(famtter)
        stream_handler.setFormatter(famtter)

        # 为logger添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

        # 配置文件写法
        # logging.config.fileConfig(LogUtils.log_conf_file, defaults={'logdir': LogUtils.log_dir, 'logfile': log_name})
        # self.logger = logging.getLogger('simpleExample')  # 根据logger的name，获取对应的logger
        # self.logger.setLevel(logging.DEBUG)

    def get_logger(self):
        return self.logger

    @classmethod
    def init_logger(cls):
        '''
        初始化logger，指定生成日志文件的路径
        :return: 返回logger对象
        '''
        if cls.logger is None:
            log_name = "run.log"
            cls.__init__(cls, log_name)

    @classmethod
    def info(cls, msg):
        cls.init_logger()
        cls.logger.info(msg=msg)

    @classmethod
    def debug(cls, msg):
        cls.init_logger()
        cls.logger.debug(msg=msg)

    @classmethod
    def error(cls, msg):
        cls.init_logger()
        cls.logger.error(msg=msg)


if __name__ == "__main__":
    # 类名方式运行，日志输出到固定文件 run.log
    LogUtils.info('info message')
    LogUtils.debug('debug message')
    LogUtils.error('error message')

    # 实例化日志输出，日志输出到指定文件下
    # log = LogUtils("root.log").get_logger()
    # log.info('root')
    # log = LogUtils("test.log").get_logger()
    # log.info('test')
    # log2 = LogUtils("test2.log").get_logger()
    # log2.debug('test2')
    # log3 = LogUtils("test3.log").get_logger()
    # log3.warning('test3')
