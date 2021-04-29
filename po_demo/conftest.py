"""
==================
Author:Chloeee
Time:2021/4/27 22:51
Contact:403505960@qq.com
==================
"""
from selenium import webdriver
from config.path import config_dir, join_dir_file
import pytest
import yaml
import time

@pytest.fixture()
def login_by_cookie():
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')

    cookie_file = join_dir_file(config_dir,"cookies_data.yaml")
    # 读取保存的cookie文件
    with open(cookie_file, "r", encoding="utf-8") as f:
        cookies = yaml.safe_load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame')
    # 等待
    driver.implicitly_wait(10)
    yield driver

    time.sleep(5)
    driver.close()


