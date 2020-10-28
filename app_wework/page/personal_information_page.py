# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : personal_information_page.py
# @Author   : Pluto.
# @Time     : 2020/10/27 21:02
from appium.webdriver.common.mobileby import MobileBy

from app_wework.page.base_page import BasePage
from app_wework.page.personal_information_setup_page import PersonalInformationSetupPage


class PersonalInformationPage(BasePage):
    _edit_element = (MobileBy.ID, "hxm")

    def go_to_personal_information_setup_page(self):
        self.find_and_click(self._edit_element)
        return PersonalInformationSetupPage(self.driver)
