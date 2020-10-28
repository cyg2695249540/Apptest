# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/10/22 19:18
from time import sleep

from selenium.webdriver.common.by import By


from web_wework.page.base_page import BasePage


class ContactPage(BasePage):
    _addmember_butto = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _cancel_member = (By.CSS_SELECTOR, ".js_btn_cancel")
    _member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

    _create_dropdown = (By.CSS_SELECTOR, ".js_create_dropdown")
    _adddepartment = (By.CSS_SELECTOR, ".js_create_party")
    _jstree_anchor = (By.CSS_SELECTOR, ".jstree-anchor")

    def go_to_addmember_page(self):
        from web_wework.page.addmember_page import AddmemberPage
        while True:
            self.find_and_click(self._addmember_butto)
            try:
                if self.find(self._cancel_member) is not None:
                    break
            except:
                print("再次点击")
        return AddmemberPage(self.driver)

    def get_member_list(self):
        self.wait_for_click(self._member_list)
        ele = self.finds(self._member_list)
        return [name.text for name in ele]

    def go_to_adddepartment_page(self):
        from web_wework.page.adddpartment_page import AddDepartmentPage
        self.find_and_click(self._create_dropdown)
        self.find_and_click(self._adddepartment)
        return AddDepartmentPage()

    def get_department_list(self):
        # self.wait_for_clickable(self._jstree_anchor)
        sleep(1)
        ele = self.finds(self._jstree_anchor)
        return [name.text for name in ele]