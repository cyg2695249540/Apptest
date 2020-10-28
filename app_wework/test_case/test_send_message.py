# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_send_message.py
# @Author   : Pluto.
# @Time     : 2020/10/24 20:00
import pytest

from app_wework.page.app import App


class TestSendMessage():
    def setup(self):
        self.app = App()
        self.main = self.app.start().go_to_main_page()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("groupname, text", [("软件测试","test001")])
    def test_send_message(self, groupname, text):
        chatext = self.main.go_to_chat().serachchat(groupname).chat(text).get_chat_list()
        assert text == chatext[-1].text
