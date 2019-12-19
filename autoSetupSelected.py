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

productsID = "5463	9373	12152	5463	8224	12152	12520	12360	12070	12511	11921	7985	6801	12512	11532	6166	12217	8731"


def addProducts(proID):
    # 点击跳转品质优选
    chromeBrowser.find_element_by_xpath(
        '//*[@class="el-tabs el-tabs--card el-tabs--top"]/div/div/div/div/div[6]'
    ).click()
    time.sleep(2)

    replacedProID = proID.replace("	", ",")

    # 点击跳转商品管理
    chromeBrowser.find_element_by_xpath(
        '//*[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[3]/td[3]/div/button[3]').click()
    time.sleep(2)

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
    # selectWindow = chromeBrowser.find_element_by_xpath('//*[@class="el-popup-parent--hidden"]/div[2]')
    # time.sleep(1)
    # selectWindow.find_element_by_xpath('//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[4]/span').click()
    # time.sleep(1)

    chromeBrowser.find_element_by_xpath('//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[4]/span[contains(text(),"50条/页")]').click()

    # # 点击全选
    # chromeBrowser.find_element_by_xpath('//*[@class="el-table el-table--fit el-table--border el-table--enable-row-hover el-table--enable-row-transition"]/div[2]/table/thead/tr/th/div/label/span').click()
    # time.sleep(1)

    # # 点击确定添加
    # chromeBrowser.find_element_by_xpath('//*[@class="app-container"]/div[4]/div/div[3]/span/button[2]').click()
    # time.sleep(1)


def sortChoicesProducts(proID):
    IDs = proID.split("	")

    for i in range(1, len(IDs) + 1):
        chromeBrowser.find_element_by_xpath(
            '//*[@class="sub-menu-content-wrapper"]/div/div/div/form/div/div/div/input'
        ).clear()
        time.sleep(1)

        chromeBrowser.find_element_by_xpath(
            '//*[@class="sub-menu-content-wrapper"]/div/div/div/form/div/div/div/input'
        ).send_keys(IDs[i - 1])
        time.sleep(1)

        chromeBrowser.find_element_by_xpath(
            '//*[@class="sub-menu-content-wrapper"]/div/div/div/form/div[3]/div/button'
        ).click()
        time.sleep(2)

        chromeBrowser.find_element_by_xpath(
            '//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr/td[3]/div/div/div/input'
        ).clear()
        time.sleep(1)

        chromeBrowser.find_element_by_xpath(
            '//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr/td[3]/div/div/div/input'
        ).send_keys(i)
        time.sleep(1)

        chromeBrowser.find_element_by_xpath(
            '//*[@class="el-table__fixed-body-wrapper"]/table/tbody/tr/td[4]/div/button/span'
        ).click()
        time.sleep(1)

        chromeBrowser.find_element_by_xpath(
            '//*[@class="el-message-box__wrapper"]/div/div[3]/button[2]/span'
        ).click()
        time.sleep(2)


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

    addProducts(productsID)

    # sortChoicesProducts(productsID)
