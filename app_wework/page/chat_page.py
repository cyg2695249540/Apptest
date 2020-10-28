# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : chat_page.py
# @Author   : Pluto.
# @Time     : 2020/10/24 20:46
from appium.webdriver.common.mobileby import MobileBy

from app_wework.page.base_page import BasePage


class ChatPage(BasePage):
    _inputbox = (MobileBy.ID, "ejs")
    _input_element = (MobileBy.ID, "ejo")
    _chatext = (MobileBy.ID, "ejd")

    def chat(self, text):
        self.find_and_send_keys(self._inputbox, text)
        self.find_and_click(self._input_element)
        return self

    def get_chat_list(self):
        chatext = self.finds(self._chatext)
        return chatext
