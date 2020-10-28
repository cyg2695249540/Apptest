# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base_page.py
# @Author   : Pluto.
# @Time     : 2020/10/22 19:18
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""

    def __init__(self, driver_base=None):
        if driver_base is None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver: WebDriver = driver_base
        if self._base_url != "":
            self.driver.get(self._base_url)
        self.driver.implicitly_wait(3)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        return self.find(locator).click()

    def find_and_send_keys(self, locator, value):
        return self.find(locator).send_keys(value)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_click(self, element):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))
