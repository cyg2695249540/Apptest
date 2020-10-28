# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_addmember.py
# @Author   : Pluto.
# @Time     : 2020/10/22 18:36
import allure
import pytest
import yaml

from web_wework.page.main_page import MainPage


def get_datas():
    with open("../datas/addcontact.yml", encoding="utf-8") as f:
        contact_datas = yaml.safe_load(f)
        addcontact = contact_datas["add"]
        case1 = contact_datas["case1"]
        addcontactfail = contact_datas["addfail"]
        case2 = contact_datas["case2"]
        return addcontact, case1, addcontactfail, case2


@allure.feature("添加成员模块")
class TestAddMember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    @allure.feature("添加成员")
    @pytest.mark.parametrize("username, acctid, phone", get_datas()[0], ids=get_datas()[1])
    def test_addmember(self, username, acctid, phone):
        namelist = self.main.go_to_addmember_page().addmember(username, acctid, phone).save_member().get_member_list()
        assert username in namelist

    @allure.feature("添加成员失败")
    @pytest.mark.parametrize("username,acctid,phone", get_datas()[2], ids=get_datas()[3])
    def test_addmember_fail(self, username, acctid, phone):
        namelist = self.main.go_to_addmember_page().addmember(username, acctid, phone).cancel_member().get_member_list()
        assert username not in namelist

    @allure.feature("通讯录添加成员")
    @pytest.mark.parametrize("username,acctid,phone", get_datas()[0], ids=get_datas()[1])
    def test_contact_addmember(self, username, acctid, phone):
        namelist = self.main.go_to_contact_page().go_to_addmember_page().addmember(username, acctid,
                                                                                   phone).save_member().get_member_list()
        assert username in namelist
