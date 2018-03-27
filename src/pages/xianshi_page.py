# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from selenium.webdriver.common.by import By
from .basepage import BasePage
import time
import logging

class XianShi(BasePage):

    #秒杀按钮
    xianshi_button = (By.LINK_TEXT, "限时折扣")

    iframe_id = 'mallmanage_index'

    #添加
    xianshiadd_btn = (By.XPATH, "//div[@class='con_hd mt10']/button[1]")


    #活动名称
    vname = (By.ID, 'vname')

    # vstartTime
    # vendTime
    #产品选择框
    productTitle = (By.ID, 'productTitle')

    #产品魔板
    product_btn = (By.NAME, "54")

    #折扣价
    zekoujia = (By.ID, 'vdiscountPrice')
    #活动库存

    kucun = (By.ID, 'vactStock')
    #活动每人限购
    xiangou = (By.ID, 'vactPurchaseLimit')

    jiage = (By.ID, 'voriginalPrice')
    kucun1 = (By.ID, 'voriginalStock')
    xiangou1 = (By.ID, 'voriginalPurchaseLimit')
    #确定
    quxiao_btn = (By.XPATH, "//div[@class='ui-dialog-button']/button[2]")
    #取消
    quxiao_btn = (By.XPATH, "//div[@class='ui-dialog-button']/button[1]")




    def add_xiashi(self):


        self.click(self.xianshi_button)

        self.switch_frame(self.iframe_id)

        self.click(self.xianshiadd_btn)

        time.sleep(5)

        self.send_keys(self.vname,'test')

        time.sleep(3)

        self.click(self.productTitle)

        time.sleep(5)
        self.click(self.product_btn)
        time.sleep(5)
        self.send_keys(self.zekoujia, '1')
        self.send_keys(self.kucun, '5')
        self.send_keys(self.xiangou, '2')
        self.send_keys(self.jiage, '3')
        self.send_keys(self.kucun1, '2')
        self.send_keys(self.xiangou1, '3')














