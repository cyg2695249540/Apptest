# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base_api.py
# @Author   : Pluto.
# @Time     : 2020/10/22 21:17
import requests
from jsonpath import jsonpath
from jsonschema import validate


class BaseApi:
    def send_requests(self, req: dict):
        return requests.request(**req)

    def base_jsonpath(self,obj, expr):
        return jsonpath(obj, expr)

    def base_jasonschema(self,instance, schema):
        return validate(instance, schema)
