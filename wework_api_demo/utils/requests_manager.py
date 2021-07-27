"""
==================
Author:Chloeee
Time:2021/7/26 21:27
Contact:403505960@qq.com
==================
"""
import json
import requests
import logging


class RequestsManager:


    def send_requests(self,method,url,**kwargs):
        try:
            response = requests.request(method, url=url, **kwargs)
        except ConnectionError as ce:
            # todo:log
            raise ce
        else:
            # 用json格式返回响应体
            response_json = response.json()
            # todo:log
            return response_json





