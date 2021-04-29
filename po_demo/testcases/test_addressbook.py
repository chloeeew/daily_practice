"""
==================
Author:Chloeee
Time:2021/4/27 22:43
Contact:403505960@qq.com
==================
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.index import IndexPage
from pages.addressbook import AddressBookPage
import yaml
import time

# todo: 把冒烟测试的所有数据随机数化，达到每次执行都能够运行
def test_add_member_smoke(login_by_cookie):
    """
    添加成员：
    1、首页点击通讯录页签  2、点击添加成员按钮  3、输入信息
    断言：提示保存成功  通讯录有该邮箱的信息
    """
    driver = login_by_cookie
    IndexPage(driver).click_tab_address_book().click_add_member_btn().\
        add_member_by_email("test","8e898","ofew2@qq.com")

    address_book = AddressBookPage(driver)
    assert address_book.get_element_by_text("保存成功")
    assert "ofew2@qq.com" in address_book.get_member_email_list


def test_add_department_smoke(login_by_cookie):
    """
    冒烟测试：添加部门
    1、首页点击通讯录  2、点击添加部门  3、输入部门名称  4、选择所属部门公司之下的著部门
    断言：提示新建部门成功 、  通讯录页面存在该部门的文件夹
    """
    driver = login_by_cookie
    IndexPage(driver).click_tab_address_book().click_add_department().input_department_info("12223")
    address_book = AddressBookPage(driver)
    assert address_book.get_element_by_text("新建部门成功")
    assert "12223" in address_book.get_department_text_list

