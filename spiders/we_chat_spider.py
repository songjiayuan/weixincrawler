import re
from requests_wrapper import requests_wrapper
from bs4 import BeautifulSoup


class Wechat_spider():

    def level1(self, response):
        print('level1')
        soup = BeautifulSoup(response.text, "lxml")
        a_link = soup.find_all(uigs="account_name_0")[0]
        a_url = a_link['href']
        print('a_url', a_url)
        self.level2(a_url)

    def level2(self, a_url):
        response = requests_wrapper(a_url)
        print('level2')
        print(response.text)
        results = re.findall('content_url":"(.*?)"', response.text)
        print(results)
        if results:
            aim_url = results[0]
            aim_url = aim_url.replace('amp;', '')
            aim_url = 'https://mp.weixin.qq.com' + aim_url
            self.level3(aim_url)
        else:
            print('level2', '无效')
            return

    def level3(self, url):
        print('level3')
        response = requests_wrapper(url)
        html_doc = BeautifulSoup(response.text, "lxml")
        title = html_doc.find('title').text
        print(title)
