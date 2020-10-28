# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/10/22 19:18
from selenium.webdriver.common.by import By

from web_wework.page.addmember_page import AddmemberPage
from web_wework.page.base_page import BasePage
from web_wework.page.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _addmember_button = (By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
    _contact_butto = (By.CSS_SELECTOR, "[id='menu_contacts']")

    def go_to_addmember_page(self):
        self.find_and_click(self._addmember_button)
        return AddmemberPage(self.driver)

    def go_to_contact_page(self):
        self.find_and_click(self._contact_butto)
        return ContactPage(self.driver)
