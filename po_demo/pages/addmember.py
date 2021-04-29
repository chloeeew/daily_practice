"""
==================
Author:Chloeee
Time:2021/4/28 20:21
Contact:403505960@qq.com
==================
"""

from common.basepage import BasePage
from selenium.webdriver.common.by import By

class AddMemberPage(BasePage):
    # 输入姓名框
    input_name_locator = (By.ID, 'username')
    # 账号框
    input_id_locator = (By.ID, 'memberAdd_acctid')
    # email框
    email_locator = (By.ID, 'memberAdd_mail')
    # 取消/勾选通知邮箱邀请
    enterprise_invitation_locator = (By.XPATH, '//*[contains(text(),"企业邀请")]/preceding-sibling::input')
    # 保存按钮
    save_btn_locator = (By.XPATH, '(//*[text()="保存"])[1]')

    def add_member_by_email(self,name, usr_id, email):
        # 输入姓名
        self.send_text(self.input_name_locator, name)
        # 输入账号
        self.send_text(self.input_id_locator, usr_id)
        # 输入邮箱
        self.send_text(self.email_locator, email)
        # 取消勾选通知邮箱邀请
        self.click_element(self.enterprise_invitation_locator)
        # 点击保存
        self.click_element(self.save_btn_locator)

        return self

