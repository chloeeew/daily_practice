"""
==================
Author:Chloeee
Time:2021/4/21 21:12
Contact:403505960@qq.com
==================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yaml


def test_add_member_by_cookie():
    """
    测试cookie（首先要复用拿到cookie才能执行这个方法）
    """
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    # 读取保存的cookie文件
    with open("data.yaml", "r", encoding="utf-8") as f:
        cookies = yaml.safe_load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame')

    # 等待
    driver.implicitly_wait(10)
    # 点击通讯录
    driver.find_element(By.ID, 'menu_contacts').click()
    # 点击上方第一个添加成员
    driver.find_element(By.XPATH, '(//*[contains(text(),"添加成员")])[1]').click()
    # 输入姓名
    driver.find_element(By.ID, 'username').send_keys("Chloeee")
    # 输入账号
    random_usr = int(time.time())
    driver.find_element(By.ID, 'memberAdd_acctid').send_keys(f'rand{random_usr}')
    # 输入邮箱
    driver.find_element(By.ID, 'memberAdd_mail').send_keys(f'{random_usr}@qq.com')
    # 取消勾选通知邮箱邀请
    driver.find_element(By.XPATH, '//*[contains(text(),"企业邀请")]/preceding-sibling::input').click()
    # 点击保存
    driver.find_element(By.XPATH, '(//*[text()="保存"])[1]').click()
    assert driver.find_element(By.XPATH, '//*[text()="保存成功"]')