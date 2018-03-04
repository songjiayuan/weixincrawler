import re
import requests
from bs4 import BeautifulSoup
from config import headers


class Wechat_spider():
    def __init__(self, response):
        self.response = response

    def level1(self):
        soup = BeautifulSoup(self.response.text, "lxml")
        a_link = soup.find_all(uigs="account_name_0")[0]
        a_url = a_link['href']
        res = requests.get(a_url, headers=headers)
        self.level2(res)

    def level2(self, response):
        results = re.findall('content_url":"(.*?)"', response.text)
        print(results)
        if results:
            aim_url = results[0]
            aim_url = aim_url.replace('amp;', '')
            aim_url = 'https://mp.weixin.qq.com' + aim_url
            res = requests.get(aim_url)
            self.level3(res)

    def level3(self, response):
        url = response.url
        html_doc = BeautifulSoup(response.text, "lxml")
        title = html_doc.find('title').text
        print(title)
        print(url)
