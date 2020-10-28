# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : addmember_detail_page.py
# @Author   : Pluto.
# @Time     : 2020/10/24 16:49
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_wework.page.base_page import BasePage


class AddmemberDetailPage(BasePage):
    _name_element = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@class='android.widget.EditText']")
    _gender_elemet = (MobileBy.XPATH, "//*[@text='男']")
    _female_element = (MobileBy.XPATH, "//*[@text='女']")
    _male_element = (MobileBy.XPATH, "//*[@text='男']")
    _phone_element = (MobileBy.XPATH,
                      "//*[contains(@text,'手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']")
    _save_element = (MobileBy.XPATH, "//*[@text='保存']")

    def add_name(self, name):
        self.find_and_send_keys(self._name_element, name)
        return self

    def add_gender(self, gander):
        self.find_and_click(self._gender_elemet)
        if gander == "女":
            self.wait_for_click(self._female_element)
            self.find_and_click(self._female_element)
        else:
            self.wait_for_click(self._male_element)
            self.find_and_click(self._male_element)
        return self

    def add_phone(self, phone):
        self.find_and_send_keys(self._phone_element, phone)
        return self

    def click_save(self):
        from app_wework.page.addmember_page import AddmemberPage
        self.find_and_click(self._save_element)
        return AddmemberPage(self.driver)
