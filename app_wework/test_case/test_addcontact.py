# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_addcontact.py
# @Author   : Pluto.
# @Time     : 2020/10/24 16:45
import pytest
import yaml

from app_wework.page.app import App


def get_datas():
    with open("../datas/addcontact.yml", encoding="utf-8") as f:
        contact_datas = yaml.safe_load(f)
        addcontact = contact_datas["add"]
        delcontact = contact_datas['del']
        return addcontact, delcontact


class TestAddcontact():
    def setup(self):
        self.app = App()
        self.main = self.app.start().go_to_main_page()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phone", get_datas()[0])
    def test_addcontact(self, name, gender, phone):
        mypage = self.main.go_to_contact().addmember().addconnect_menual().add_name(name).add_gender(
            gender).add_phone(phone).click_save()
        mytost = mypage.get_toast()
        assert mytost == "添加成功"
