"""
==================
Author:Chloeee
Time:2021/4/27 23:00
Contact:403505960@qq.com
==================
"""

from common.basepage import BasePage
from selenium.webdriver.common.by import By
from pages.addmember import AddMemberPage

class AddressBookPage(BasePage):
    # 上方的添加成员
    add_member_btn_locator = (By.XPATH, '(//*[contains(text(),"添加成员")])[1]')
    # 加号
    add_btn_locator = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
    # 添加部门按钮
    add_department_locator = (By.XPATH, '//*[contains(text(),"添加部门")]')

    def click_add_member_btn(self):
        self.click_element(self.add_member_btn_locator)
        return AddMemberPage(self.driver)

    def click_add_department(self):
        self.click_element(self.add_btn_locator)
        self.click_element(self.add_department_locator)
        return self

    @property
    def get_member_email_list(self):
        member_list_locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(6) > span")
        return self.get_elements_text_list(member_list_locator)

    def input_department_info(self, name, index=0):
        # todo:index等于0默认是公司
        department_name_locator = (By.XPATH, '//*[contains(text(),"部门名称")]/following-sibling::input')
        self.send_text(department_name_locator, name)
        department_type_locator = (By.XPATH, '//*[contains(text(),"所属部门")]//following-sibling::a')
        self.click_element(department_type_locator)
        company_folder_locator = (By.XPATH, '//*[contains(text(),"所属部门")]//following-sibling::div//a[text()="测试"]')
        self.click_element(company_folder_locator)
        confirm_btn = (By.XPATH, '//*[contains(text(),"确定")]')
        self.click_element(confirm_btn)
        return self


    @property
    def get_department_text_list(self):
        department_list_locator = (By.XPATH, '//a[text()="测试"]/following-sibling::ul/li')
        return self.get_elements_text_list(department_list_locator)


