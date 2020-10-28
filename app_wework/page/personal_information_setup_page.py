# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : personal_information_setup_page.py
# @Author   : Pluto.
# @Time     : 2020/10/27 21:09
from appium.webdriver.common.mobileby import MobileBy

from app_wework.page.base_page import BasePage
from app_wework.page.edit_member_page import EditMemberPage


class PersonalInformationSetupPage(BasePage):
    _edit_member_element=(MobileBy.XPATH,"//*[@text='编辑成员']")
    def go_to_edit_member_page(self):
        self.find_and_click(self._edit_member_element)
        return EditMemberPage(self.driver)