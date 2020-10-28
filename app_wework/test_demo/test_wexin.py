# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_wexin.py
# @Author   : Pluto.
# @Time     : 2020/10/24 12:25
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def get_datas():
    with open("../datas/addcontact.yml", encoding="utf-8") as f:
        contact_datas = yaml.safe_load(f)
        addcontact = contact_datas['add']
        delcontact = contact_datas['del']
    return addcontact, delcontact


class TestWeiXin:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        # 不清除数据
        caps["noReset"] = True
        # 不重启应用
        caps["dontStopAppOnReset"] = True
        # 等待页面空闲的时间
        caps['settings[waitForIdleTimeout]'] = 1
        # 跳过安装，权限设置等操作
        caps["skipDeviceInitialization"] = True
        # 设置可输入中文
        caps["unicodekeyBoard"] = True
        caps["resetkeyBoard"] = True
        # 自动判断弹框
        caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_send_message(self):
        _sendTtext = "test001"
        el1 = self.driver.find_element(MobileBy.ID, "hxw")
        el1.click()
        el2 = self.driver.find_element_by_id("ghu")
        el2.send_keys("软件测试")
        el3 = self.driver.find_element(MobileBy.XPATH,
                                       "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView")
        el3.click()
        el4 = self.driver.find_element_by_id("ejs")
        el4.send_keys(_sendTtext)
        el5 = self.driver.find_element_by_id("ejo")
        el5.click()
        elements = self.driver.find_elements_by_id("ejd")
        assert _sendTtext == elements[-1].text

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滚动获取元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.ID, "hiy").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        result = self.driver.find_element(MobileBy.ID, "os").text
        assert "外出打卡成功" == result

    @pytest.mark.parametrize('name,gander,phonenum', get_datas()[0])
    def test_addcontact(self, name, gander, phonenum):
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/ec6' and @text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # 滚动获取添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/..//*[@class='android.widget.EditText']").send_keys(
            name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gander == "女":
            _searchtext = (MobileBy.XPATH, "//*[@text='女']")
            element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(_searchtext))
            element.click()
        else:
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='男']"))
            element.click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']").send_keys(
            phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # sleep(2)
        # # 获取网页源代码，寻找Toast
        # print(self.driver.page_source)
        mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert mytoast == "添加成功"

    @pytest.mark.parametrize('name', get_datas()[1])
    def test_deletecontact(self, name):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hxw").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ghu").send_keys(name)
        sleep(2)
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        before = len(eles)
        if before == 1:
            print("没有可删除人员")

        else:
            # self.driver.find_element(MobileBy.XPATH,
            #                          f"//*[@text='{name}' and @class='android.widget.TextView']").click()
            eles[1].click()
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hxm").click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("删除成员").instance(0));').click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
            sleep(5)
            eles2 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
            after = len(eles2)
            assert after == before - 1
