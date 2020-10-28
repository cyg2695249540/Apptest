# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : addmember_page.py
# @Author   : Pluto.
# @Time     : 2020/10/24 16:49
from appium.webdriver.common.mobileby import MobileBy

from app_wework.page.addmember_detail_page import AddmemberDetailPage
from app_wework.page.base_page import BasePage


class AddmemberPage(BasePage):
    _addmember_element=(MobileBy.XPATH, "//*[@text='手动输入添加']")
    def addconnect_menual(self):
        self.find_and_click(self._addmember_element)
        return AddmemberDetailPage(self.driver)

    def get_toast(self):
        mytoast = self.get_toast_text()
        return mytoast