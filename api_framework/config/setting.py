# !/usr/bin python3                                 
# encoding   :utf-8 -*-                            
# @author    :贾克沣                              
# @software  :PyCharm      
# @file      :setting.py
import os


class Config:
    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据路径
    data_path = os.path.join(root_path, 'data/cases.xlsx')

    # 测试文件路径
    case_path = os.path.join(root_path, 'test_cases')

    # 测试报告路径
    report_path = os.path.join(root_path, 'report')
    if not os.path.exists(report_path):  # 如果没用文件判断是否生成
        os.mkdir(report_path)

    # 日志文件夹
    log_path = os.path.join(root_path, 'log')
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    logger_path = os.path.join(log_path,'log_da.txt')

    # 日志名称
    logger_name = 'NN_logger'

    # config 路径
    config_path = os.path.join(root_path,'config')

    # yaml路径
    yaml_path = os.path.join(config_path,'configset.yaml')


class DevConfig(Config):
    # 项目的域名
    host = 'http://120.290.12'


config = Config()
