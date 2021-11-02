# !/usr/bin python3                                 
# encoding   :utf-8 -*-                            
# @author    :贾克沣                              
# @software  :PyCharm      
# @file      :test_register.py
import json
import unittest

import db
import ddt

from api_framework.common.generate_mobile import generate_mobile
from api_framework.common.log_handler import LoggerHandler
from api_framework.common.demo_excel_handler import ExcelHandler
from api_framework.common.requests_handler import RequestsHandler

from api_framework.config.setting import config

logger = LoggerHandler(name=config.logger_name,file=config.logger_path)


@ddt.ddt
class TestRegister(unittest.TestCase):
    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read_all("regesir")

    def setUp(self) -> None:
        self.req = RequestsHandler()

    def tearDown(self) -> None:
        self.req.close_session()

    @ddt.data(*data)
    def test_register(self, test_data):
        if "#exist_phone" in test_data['json']:
            mobile = generate_mobile()
            # 查询数据库
            # mobile = db.find('select....')

            # 替换
            test_data['json'] = test_data['json'].replace("#exist_phone",mobile)

        # 访问接口获取实际值
        res = self.req.visit(config.host + test_data['url'],
                             test_data['method'],
                             json=json.loads(test_data['json']),
                             headers=json.loads(test_data['headers'])
                             )
        # 获取预期结果 test_data['expected']

        # 断言
        try:
            self.assertEqual(eval(test_data['expected'])['code'],res['code'])
            # 写入excel数据
            self.excel_handler.write(config.data_path,
                                     'regesir',
                                     test_data['case_id']+1,
                                     9,
                                     '测试通过')
        except AssertionError as f:
            self.logger.error("测试用例失败:{}".format(f))
            # 手动抛出异常，否则测试用例会自动通过
            self.excel_handler.write(config.data_path,
                                     'regesir',
                                     test_data['case_id'] + 1,
                                     9,
                                     '测试不通过')
            raise f

        # 如果出现断言失败，要将失败的用例记录到logger当中









