# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/10/24 16:48
from appium.webdriver.common.mobileby import MobileBy

from app_wework.page.addmember_page import AddmemberPage
from app_wework.page.base_page import BasePage
from app_wework.page.search_page import SearchPage


class ContactPage(BasePage):
    _addmemeber_text = "添加成员"
    _search_element=(MobileBy.ID,"hxw")

    def addmember(self):
        self.find_by_scroll_and_click(self._addmemeber_text)
        return AddmemberPage(self.driver)

    def go_to_search_page(self):
        self.find_and_click(self._search_element)
        return SearchPage(self.driver)
