# !/usr/bin python3                                 
# encoding   :utf-8 -*-                            
# @author    :贾克沣                              
# @software  :PyCharm      
# @file      :log_handler.py
# @Time      :2021/6/9 0:34
import logging

from api_framework.common.yaml_handler import yaml_data
from api_framework.config.setting import config

dy = yaml_data


class LoggerHandler(logging.Logger):

    def __init__(self,
                 name='python_logger',
                 level='DEBUG',
                 file=None,
                 fmtt='%(name)s-%(levelname)s-%(message)s-%(lineno)d'
                 ):
        # Logger(name)
        # logger = logging.getLogger(name)
        super().__init__(name)

        # 设置级别
        self.setLevel(level)

        fmt = logging.Formatter(fmtt)
        # 初始化处理器
        if file:
            file_handler = logging.FileHandler(file)
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)

        stream_handler = logging.StreamHandler()

        # 设置handler 的级别
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


logger = LoggerHandler(name=config.logger_name,file=config.logger_path)
# logger = LoggerHandler(name=data['logger']['name'],file=data['logger']['file'])

if __name__ == '__main__':

    logger.debug('hello')
