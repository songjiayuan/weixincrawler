from requests_wrapper import requests_wrapper
from rules.wechat_name import wechat_name_list
from time import sleep
from spiders.we_chat_spider import Wechat_spider
import requests

for index, name in enumerate(wechat_name_list[0:20]):
    we_url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&query=' + name
    try:
        res = requests_wrapper(we_url)
    except requests.exceptions.ConnectionError:
        res.status_code = "Connection refused"

    print(index)
    try:
        res.encoding = 'utf-8'
        new_wechat_spider = Wechat_spider()
        new_wechat_spider.level1(res)
    except:
        print(res)
    sleep(3)
