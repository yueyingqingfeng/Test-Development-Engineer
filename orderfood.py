from random import  randint
from datetime import datetime
import requests
from config import *

class orderFood():
    """
    定时任务，自动抽取餐厅，懒人点餐。
    """
    #随机抽取餐厅
    def canteen(self):

        # for i in range(20):
        # print(len(ct))
        rdm = randint(0,len(ct)-1)
        # print(ct[rdm])
        return ct[rdm]

    #判断是否周末
    def isweek(self):

        today = datetime.now().weekday() + 1

        # print(today)
        #测试星期几
        # week = datetime.strptime("20211122", "%Y%m%d").weekday() + 1
        # print(week)
        if today <=5:
            return today
        return '周末'

    #生成内容
    def content(self):
        if orderFood.isweek() == '周末':
            content = "今天周末：" \
                      "小伙伴们好好玩耍~\(≧▽≦)/~"

            return content
        else:
            content = "上班辛苦拉!" \
                      "今天推荐餐厅:{}".format(orderFood.canteen())
            print(content)
            return content

    #调用接口
    def run(self):
        content = orderFood.content()
        # content = "你好"
        headers = {
            'content-type': 'application/json'
        }
        data = '{"msg_type":"text","content":{"text":"%s"}}' % content
        # print(data)
        # rsp = requests.post(feishuurl, headers= headers, data= data.encode('utf-8'))
        requests.post(feishuurl, headers= headers, data= data.encode('utf-8'))
        # print(rsp)

if __name__ == '__main__':
    orderFood = orderFood()
    # orderFood.canteen()
    # orderFood.isweek()
    # orderFood.content()
    orderFood.run()