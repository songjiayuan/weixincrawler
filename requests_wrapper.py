import requests
from config import headers
from time import sleep


def get_ip():
    try:
        sleep(2)
        n = requests.get('http://api.ip.data5u.com/dynamic/get.html?order=e99d8488223f1a43f9ba34e89e598ae4&sep=3')
        print('更换ip', n.text.strip())
        return n.text.strip()
    except:
        get_ip()


proxies = {
    "http": get_ip()
}


def requests_wrapper(url):
    basic_response = requests.get(url, headers, proxies=proxies, allow_redirects=False)
    print('当前请求链接：', basic_response.url)
    print('当前状态码', basic_response.status_code)
    if 'antispider' in basic_response.url:
        print('反爬虫', basic_response.url)
        proxies['http'] = get_ip()
        requests_wrapper(url)
    elif basic_response.status_code != 200:
        proxies['http'] = get_ip()
        requests_wrapper(url)
    elif '请输入验证码' in basic_response.text:
        proxies['http'] = get_ip()
        requests_wrapper(url)
    else:
        print('正常')
        print(basic_response.url)
        return basic_response
