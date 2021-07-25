"""
==================
Author:Chloeee
Time:2021/7/24 17:35
Contact:403505960@qq.com
==================
"""
import json
import mitmproxy.http
from mitmproxy import ctx
from mitmproxy import http

class HTTPEvents:
    """"""

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
        The full HTTP request has been read.
        """
        # map local
        # 赶在response前把内容改好了
        if '/v5/stock/batch/quote.json?_t=' in flow.request.url and 'x=' in flow.request.url:
            with open(r'E:\daily_practice\mock_test\stock.json',mode="r",encoding="utf-8") as f:
                data_dict = json.loads(f.read())
                new_data = recursion(data_dict,2)
                # response是None所以需要创造一个response并赋值
                flow.response = http.HTTPResponse.make(200,json.dumps(new_data))


    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
        The full HTTP response has been read.
        """
        # 设置mock规则
        if '/v5/stock/batch/quote.json?_t=' in flow.request.url and 'x=' in flow.request.url:

            data_dict = json.loads(flow.response.text)
            percent_data_list = [0,0.01,-0.01]
            for i in range(len(data_dict["data"]["items"])):
                print("REWRITE中")
                person_ind = i % len(percent_data_list)
                data_dict["data"]["items"][i]["quote"]["percent"] = percent_data_list[person_ind]


            flow.response.text = json.dumps(data_dict)



def recursion(data,times=1):
    """递归方式把所有浮点数倍增"""
    if isinstance(data,dict):
        for k,v in data.items():
            data[k] = recursion(v,times)
    elif isinstance(data,list):
        data = [recursion(i,times) for i in data]
    elif isinstance(data,float):
        return data*times
    else:
        # 非浮点数不做任何处理
        return data
    return data


addons = [
    HTTPEvents()
]


if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '9999', '-s', __file__])
