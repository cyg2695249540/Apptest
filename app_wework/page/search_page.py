# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : search_page.py
# @Author   : Pluto.
# @Time     : 2020/10/24 20:48
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app_wework.page.base_page import BasePage
from app_wework.page.chat_page import ChatPage
from app_wework.page.personal_information_page import PersonalInformationPage


class SearchPage(BasePage):
    _search_element = (MobileBy.XPATH, "//*[@text='搜索']")
    _search_name = (MobileBy.XPATH, "//*[@text='LCQ']")

    def serachchat(self, groupname):
        # group = (MobileBy.XPATH, "//*[@text='软件测试']")
        self.find_and_send_keys(self._search_element, groupname)
        sleep(5)
        group = (MobileBy.XPATH, f"//*[@text='{groupname}']")
        groupnamelist = self.finds(group)
        print(groupnamelist)
        if len(groupnamelist) < 2:
            print("没有查到")
        else:
            groupnamelist[1].click()
        return ChatPage(self.driver)

    def searchcontact(self):
        self.find_and_send_keys(self._search_element, "LCQ")
        sleep(1)
        eles = self.finds(self._search_name)
        l1 = len(eles)
        if l1 == 1:
            print("没有该联系人")
        else:
            eles[1].click()
        return PersonalInformationPage(self.driver)
