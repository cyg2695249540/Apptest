# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/10/24 16:48
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app_wework.page.base_page import BasePage
from app_wework.page.contact_page import ContactPage
from app_wework.page.search_page import SearchPage


class MainPage(BasePage):
    _contact_element = (MobileBy.XPATH,
                        "//*[@resource-id='com.tencent.wework:id/ec6' and @text='通讯录']")
    _find_element = (MobileBy.ID, "hxw")

    def go_to_contact(self):
        self.find_and_click(self._contact_element)
        return ContactPage(self.driver)

    def go_to_chat(self, ):
        self.find_and_click(self._find_element)
        return SearchPage(self.driver)

    def goto_workbench(self):
        pass
