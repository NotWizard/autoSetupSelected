# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   自动配置品质优选.py
@Time    :   2019/09/07 10:25:58
@Author  :   XXX
@Version :   1.0
@Contact :   notwizardx@gmail.com
@Desc    :   None
'''

# here put the import lib
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

productsID = "447200784958885889	8301	449556520485531648	444400192607760385	11508​	13396	11282	13072	446550240158298112	5436	10449	446977751623143424	12565	12899	12270	451583945465671680	12788	11665	11351	444458706348806145	11290	12440	7568	12545	8517	9009	9647	451574877489475585	7985	10144"


def addProducts(proID):

    replacedProID = proID.replace("	", ",")

    # 点击新增
    chromeBrowser.find_element_by_xpath('//*[@class="app-container"]/div/form[2]/div/div/button').click()
    time.sleep(1)

    # 输入商品IDs
    chromeBrowser.find_element_by_xpath('//*[@class="el-dialog__body"]/div/form/div/div/div/div/input').send_keys(replacedProID)
    time.sleep(1)

    # 点击搜索
    chromeBrowser.find_element_by_xpath('//*[@class="el-dialog__body"]/div/form/div[2]/div/div/button').click()
    time.sleep(1)

    # 滚动页面
    # js = "window.scrollTo(0,document.body.scrollHeight);"
    # chromeBrowser.execute_script(js)
    # time.sleep(1)

    # 点击选择页数
    chromeBrowser.find_element_by_xpath('//*[@class="editGoodsGounp"]/div[2]/div/span/div').click()
    time.sleep(1)

    # 点击选择一页展示50个
    chromeBrowser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[4]/span').click()
    time.sleep(1)

    # 点击全选
    chromeBrowser.find_element_by_xpath('//*[@class="el-table el-table--fit el-table--border el-table--enable-row-hover el-table--enable-row-transition"]/div[2]/table/thead/tr/th/div/label/span').click()
    time.sleep(1)

    # 点击确定添加
    chromeBrowser.find_element_by_xpath('//*[@class="app-container"]/div[4]/div/div[3]/span/button[2]').click()
    time.sleep(1)


def sortChoicesProducts(proID):
    IDs = proID.split("	")

    for i in range(1, len(IDs) + 1):
        # 清空商品ID输入框
        chromeBrowser.find_element_by_xpath(
            '//*[@class="app-container"]/div/form/div/div/div/input'
        ).clear()
        time.sleep(1)

        # 输入商品ID
        chromeBrowser.find_element_by_xpath(
            '//*[@class="app-container"]/div/form/div/div/div/input'
        ).send_keys(IDs[i - 1])
        time.sleep(1)

        # 点击搜索
        chromeBrowser.find_element_by_xpath(
            '//*[@class="app-container"]/div/form/div[3]/div/button'
        ).click()
        time.sleep(2)

        if isElementExist('//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr/td[3]/div/div/div/input'):
            # 清空商品的当前排序
            chromeBrowser.find_element_by_xpath(
                '//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr/td[3]/div/div/div/input'
            ).clear()
            time.sleep(1)

            # 输入商品的本应该排序
            chromeBrowser.find_element_by_xpath(
                '//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr/td[3]/div/div/div/input'
            ).send_keys(i)
            time.sleep(1)

            # 点击保存排序
            chromeBrowser.find_element_by_xpath(
                '//*[@class="el-table__fixed-body-wrapper"]/table/tbody/tr/td[4]/div/button/span'
            ).click()
            time.sleep(1)
        else:
            print("There do not have this product %s", IDs[i - 1])
            continue


# 判断元素是否存在
def isElementExist(xpath):
    flag = True
    try:
        chromeBrowser.find_element_by_xpath(xpath)
        return flag
    except Exception:
        flag = False
        return flag


if __name__ == "__main__":
    chromeBrowser = webdriver.Chrome()
    chromeBrowser.get('https://boss.fingo.shop/#/marketingCenter/appSet')
    time.sleep(2)

    chromeBrowser.find_element_by_xpath(
        '//*[@class="login-container"]/form/div/div/div/input').send_keys(
            'xiangjie')
    chromeBrowser.find_element_by_xpath(
        '//*[@class="login-container"]/form/div[2]/div/div/input').send_keys(
            '123456')
    # 点击登陆
    chromeBrowser.find_element_by_xpath(
        '//*[@class="login-container"]/form/div[3]/div/button').click()
    time.sleep(2)

    # 点击折叠打开运营管理
    chromeBrowser.find_element_by_xpath(
        '//*[@class="layout-nav-wrapper"]/div/ul/li[2]/div').click()
    time.sleep(1)

    # 点击跳转App配置
    chromeBrowser.find_element_by_xpath(
        '//*[@class="layout-nav-wrapper"]/div/ul/li[2]/ul/li/a/span').click(
        )
    time.sleep(2)

    # 点击跳转品质优选
    chromeBrowser.find_element_by_xpath(
        '//*[@class="el-tabs el-tabs--card el-tabs--top"]/div/div/div/div/div[6]'
    ).click()
    time.sleep(2)

    # 点击跳转马来商品管理
    chromeBrowser.find_element_by_xpath(
        '//*[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[3]/td[3]/div/button[3]').click()
    time.sleep(2)

    # addProducts(productsID)

    sortChoicesProducts(productsID)
