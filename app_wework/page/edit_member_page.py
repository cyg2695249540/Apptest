# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : edit_member_page.py
# @Author   : Pluto.
# @Time     : 2020/10/27 21:16
from appium.webdriver.common.mobileby import MobileBy

from app_wework.page.base_page import BasePage


class EditMemberPage(BasePage):
    _right_element = (MobileBy.XPATH, "//*[@text='确定']")

    def delete_member(self):
        from app_wework.page.personal_information_setup_page import PersonalInformationSetupPage
        self.find_by_scroll_and_click("删除成员")
        self.find_and_click(self._right_element)

