import requests
from rules.wechat_name import wechat_name_list
from time import sleep
from spiders.we_chat_spider import Wechat_spider
from config import headers

for index, name in enumerate(wechat_name_list[0:20]):
    we_url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&query=' + name
    res = requests.get(we_url, headers=headers)
    res.encoding = 'utf-8'
    print(index)
    new_wechat_spider = Wechat_spider(res)
    new_wechat_spider.level1()
    sleep(3)
