# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base_page.py
# @Author   : Pluto.
# @Time     : 2020/10/24 16:47
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_send_keys(self, locator, value):
        self.find(locator).send_keys(value)

    def find_and_get_text(self, locator):
        return self.find(locator).text

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_click(self, element):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))

    def find_by_scroll_and_click(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiScrollable(new UiSelector()'
               '.scrollable(true).instance(0))'
               '.scrollIntoView(new UiSelector()'
               f'.text("{text}").instance(0));')
        return self.find_and_click(ele)

    def get_toast_text(self):
        ele = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        return self.find_and_get_text(ele)
