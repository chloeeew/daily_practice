"""
==================
Author:Chloeee
Time:2021/4/27 22:54
Contact:403505960@qq.com
==================
"""

from common.basepage import BasePage
from selenium.webdriver.common.by import By
from pages.addressbook import AddressBookPage

class IndexPage(BasePage):
    __tab_address_book = (By.ID, 'menu_contacts')

    def click_tab_address_book(self):
        """点击通讯录"""
        self.click_element(self.__tab_address_book)
        return AddressBookPage(self.driver)


