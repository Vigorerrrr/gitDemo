# !/usr/bin python3                                 
# encoding   :utf-8 -*-                            
# @author    :贾克沣                              
# @software  :PyCharm      
# @file      :yaml_handler.py
import yaml
from api_framework.config.setting import config


class YamlHandler:
    def __init__(self,file):
        self.file = file

    def read_yaml(self):

        f = open(self.file,encoding='utf-8')
        # TODO:f.read() 和 f 都可以
        yy_data = yaml.load(f,Loader=yaml.FullLoader)
        f.close()
        return yy_data


yaml_data = YamlHandler(config.yaml_path).read_yaml()


if __name__ == '__main__':
    data = YamlHandler(config.yaml_path).read_yaml()
    print(data)