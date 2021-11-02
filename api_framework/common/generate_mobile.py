# !/usr/bin python3                                 
# encoding   :utf-8 -*-                            
# @author    :贾克沣                              
# @software  :PyCharm      
# @file      :generate_mobile.py

import random


def generate_mobile():
    """随机生成一个手机号码"""
    phone = '1' + random.choice(['3', '5', '7', '9'])
    for i in range(9):
        num = random.randint(0, 9)
        phone += str(num)
        print(phone)

    return phone
