#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os

# 定义配置项
class Config:
    BaseDir = os.getcwd()  # 获取当前这个项目的目录 如:c\user\test\Desktop\baseline\
    DB_FILE = os.path.join(BaseDir, 'baseline.sqlite')  # db_file 是数据库的完整路径,如 c:\user\test\Desktop\baseline\baseline.sqlite
    SECRET_KEY = os.urandom(24)  # flask用于对cookie进行加密的密钥 SECRET_KEY，使用urandom函数自动生成
    MAX_CONTENT_LENGTH = 300 * 1024 * 1024  # 设置的最大的http请求最大值，因为有个文件上传，限制了这个上传不能超过300M


# 注册默认配置
config = {
    'default': Config
}
