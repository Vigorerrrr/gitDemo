# !/usr/bin python3                                 
# encoding   :utf-8 -*-                            
# @author    :贾克沣                              
# @software  :PyCharm      
# @file      :run_test.py

import time
import unittest
import os

from config.HTMLTestRunner import HTMLTestRunner
from config.setting import config


loader = unittest.TestLoader()
suite = loader.discover(config.case_path)
# suite_1 = testloader.loadTestsFromModule()

# 测试报告
ts = str(int(time.time()))
file_name = 'test_report_{}.html'.format(ts)
file_path = os.path.join(config.report_path,file_name)

# with open(file_path,"w",encoding='utf-8') as f:
#
#     runner = unittest.TextTestRunner(f)

with open(file_path,'wb') as f:
    runner = HTMLTestRunner(f,title='测试报告',description='JJK测试报告',tester='Nemoss')

    runner.run(suite)