# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_deletecontact.py
# @Author   : Pluto.
# @Time     : 2020/10/27 15:35
from app_wework.page.app import App


class TestDeletecontact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().go_to_main_page()

    def teardowm(self):
        self.app.stop()

    def test_deletecontact(self):
        self.main.go_to_contact().go_to_search_page().searchcontact(
        ).go_to_personal_information_setup_page().go_to_edit_member_page().delete_member()
