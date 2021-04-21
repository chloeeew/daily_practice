"""
==================
Author:Chloeee
Time:2021/4/20 22:03
Contact:403505960@qq.com
==================
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yaml


# 复用浏览器
def test_wework():
    """
    测试已经打开并登录的企业微信
    切换到通讯录
    """
    opt = webdriver.ChromeOptions()
    # 设置debug地址
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    # 点击通讯录页签
    contact_el = driver.find_element(By.ID,'menu_contacts')
    contact_el.click()

    # 获取当前的cookie信息
    usr_cookie = driver.get_cookies()
    with open("data.yaml", "w", encoding="utf-8") as f:
        yaml.dump(usr_cookie, f)
    assert True


def test_cookie():
    driver = webdriver.Chrome()
    # 访问扫码登录页面
    # 如果不先访问登录的域名网站，那么会导致cookie失败（看cookie的domain）
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    # 获取cookie的时候，先存到yaml中，然后再读取也可以
    cookies = [{'domain': '.qq.com', 'expiry': 1619008416, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'expiry': 1619094585, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.894111186.1618920314'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'v0310RlBfbyTFVVP3C7E5HY4RYjS25h_zEowmJiI7z4LVhXX6my7IuLodLud4pC4'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a2723133'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850571997254'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850571997254'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '2548114432'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '5872691208'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325068449420'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1619007918'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '38149407841518306'}, {'domain': 'work.weixin.qq.com', 'expiry': 1619039453.61922, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '1r0gg74'}, {'domain': '.qq.com', 'expiry': 1619875789, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '403505960'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'nV_cR-K9mgCKOH4qwqnNRPEHLFCPAsOK8__zTgQopNRvVvh682-2MWbJiyrvOR5AM1G1h4yfj2cKJsu-qMMIxZteCTd3gkKL7pGLAs9yJ0qr9Xf-PKPd3QmyRL1zeViH0ktFjIh8pAcbYALDKD-dWh3DG17Z9yHBceH7SaBSbC42F7NeZFHKWyh0_fcieeMso3TexxZ6nOpqcorfHJn9Xz1UVnxue7aWbkGDGcw77__r1xmIjyD4tSwHAyjJ_ignFHYx9Gtq5mTToxEvUr8vdQ'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650543918, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618920314,1618926758,1619007918'}, {'domain': '.qq.com', 'expiry': 1909667441.177649, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_403505960'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '403505960'}, {'domain': '.qq.com', 'expiry': 2147483647.145198, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '224b72e3606a3a303ebaf01955bf0869f48fe63fba7fbffe642df7f500f4a054'}, {'domain': '.qq.com', 'expiry': 2147483647.855961, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'fKSYeDcW+o'}, {'domain': '.qq.com', 'expiry': 1682080185, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1801194509.1580695821'}, {'domain': '.work.weixin.qq.com', 'expiry': 1621600187.569104, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1908442066, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': 'f680a6665e2d89e1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650456140.297382, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}]
    # cookies里面是一个个字典值，cookies信息很多，通过遍历添加到driver中
    for cookie in cookies:
        # 设置cookie
        driver.add_cookie(cookie)
    # 登录后要访问的地址
    driver.get('https://work.weixin.qq.com/wework_admin/frame')
    time.sleep(5)
    assert True


def test_cookie_v2():
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    # 读取保存的cookie文件
    with open("data.yaml", "r", encoding="utf-8") as f:
        cookies = yaml.safe_load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.get('https://work.weixin.qq.com/wework_admin/frame')
