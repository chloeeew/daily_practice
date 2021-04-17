"""
==================
Author:Chloeee
Time:2021/4/14 20:19
Contact:403505960@qq.com
==================
"""

import yaml


def read_yaml(fpath):
    """
    :param fpath: yaml路径
    :return: yaml里的数据
    """
    with open(fpath, encoding="utf-8") as f:
        data = yaml.load(f, yaml.FullLoader)
        return data

